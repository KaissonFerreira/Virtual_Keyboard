from typing import final
import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)

keys = [["Q",'E','R','T','Y','U','I','O','P','-'],
        ['A','S','D','F','G','H','J','K','L','/'],
        ['Z','X','C','V','B','N','M',',','.',' ']]

final_text = ""

def drawALL (img, buttonList):
    for button in buttonList:
        x, y = button.position
        w, h = button.size
        cv2.rectangle(img, button.position, (x + w, y + h), (250,30,15), cv2.FILLED) # Rectangle
        cv2.putText(img, button.text, (x+10,y+30), 
        cv2.FONT_HERSHEY_PLAIN, 2,(255,255,255), 2)
    return img


class Button():
    def __init__(self, position, text, size=[45,45]):
        self.position = position
        self.size = size
        self.text = text

buttonList = []
for i in range(len(keys)):
    for j,key in enumerate(keys[i]):
        buttonList.append(Button([50*j+75,50*i+60], key)) # Movimentation of keyboard

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"] #list of 21 Landmarks points
        bbox1 = hand1["bbox"] # Bouding Box Info x,y,w,h
        centerpoint1 = hand1['center'] # center of the hand cx,cy
        handType1 = hand1["type"]# Hand type left or right
        img = drawALL(img, buttonList)
        
        if lmList1:
            for button in buttonList:
                x, y = button.position
                w, h = button.size

                if x < lmList1[8][0] <x+w and y< lmList1[8][1] <y+h:
                    cv2.rectangle(img, button.position, (x + w, y + h), (175,0,175), cv2.FILLED) # Rectangle
                    cv2.putText(img, button.text, (x+10,y+30), 
                                cv2.FONT_HERSHEY_PLAIN, 2,(255,255,255), 2)
                    l, _, _ = detector.findDistance(lmList1[8],lmList1[4],img) # l define a distância entre os dedos da posição 8 e 12 ; No Draw
                    print(l)

                    # when clicked
                    if l < 30:
                        cv2.rectangle(img, button.position, (x + w, y + h), (0,255,0), cv2.FILLED) # Rectangle
                        cv2.putText(img, button.text, (x+10,y+30), 
                                    cv2.FONT_HERSHEY_PLAIN, 2,(255,255,255), 2)
                        final_text += button.text
                        sleep(0.8)
    # Inserindo o texto na tela
    cv2.rectangle(img, (20, 400), (700,450), (128,0,0), cv2.FILLED) # Rectangle
    cv2.putText(img, final_text, (30,440), 
                cv2.FONT_HERSHEY_PLAIN, 2,(255,255,255), 2)                                
    #if len(hands) == 2:
   #     hand2 = hands[1]
    #    lmList2 = hand2["lmList"] #list of 21 Landmarks points
    #    bbox2 = hand2["bbox"] # Bouding Box Info x,y,w,h
   #     centerpoint2 = hand2['center'] # center of the hand cx,cy
   #     handType2 = hand2["type"]# Hand type left or right
  #      img = drawALL(img, buttonList)
  #      if lmList2:
  #          for button in buttonList:
  #              x, y = button.position
  #              w, h = button.size

    #            if x < lmList2[8][0] <x+w:
  #                  cv2.rectangle(img, button.position, (x + w, y + h), (0,255,0), cv2.FILLED) # Rectangle
   #                 cv2.putText(img, button.text, (x+10,y+30), 
   #                             cv2.FONT_HERSHEY_PLAIN, 2,(255,255,255), 2)

                    



    cv2.imshow("Image", img)
    cv2.waitKey(1)