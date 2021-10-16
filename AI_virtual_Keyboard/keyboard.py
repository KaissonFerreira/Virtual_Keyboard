import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)

class Button():
    def __init__(self, position, text, size=[100,100]):
        self.position = position
        self.size = size
        self.text = text
    def draw(self, img):
        cv2.rectangle(img, self.position, self.size, (250,30,15), cv2.FILLED)
        cv2.putText(img, self.text, (self.position[0]+25,self.position[1]+25), 
        cv2.FONT_HERSHEY_PLAIN, 5,(255,255,255), 3)
        return img


mybutton = Button([100,100], "Q")

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"] #list of 21 Landmarks points
        bbox1 = hand1["bbox"] # Bouding Box Info x,y,w,h
        centerpoint1 = hand1['center'] # center of the hand cx,cy
        handType1 = hand1["type"]# Hand type left or right

    if len(hands) == 2:
        hand2 = hands[1]
        lmList2 = hand2["lmList"] #list of 21 Landmarks points
        bbox2 = hand2["bbox"] # Bouding Box Info x,y,w,h
        centerpoint2 = hand2['center'] # center of the hand cx,cy
        handType2 = hand2["type"]# Hand type left or right
    
    mybutton.draw(img)

   # cv2.rectangle(img, (100,100), (200,200), (250,30,15), cv2.FILLED)
    #cv2.putText(img, "Q", (115,170), cv2.FONT_HERSHEY_PLAIN,5,(255,255,255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)