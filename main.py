import cv2
from cvzone.HandTrackingModule import HandDetector


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8, maxHands=2)


while True:
    success, img = cap.read()
    hands, img = detector.findHands(img) #with Draw
    #hands = detector.findHands(img, draw=False) # No Draw
    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"] #list of 21 Landmarks points
        bbox1 = hand1["bbox"] # Bouding Box Info x,y,w,h
        centerpoint1 = hand1['center'] # center of the hand cx,cy
        handType1 = hand1["type"]# Hand type left or right

        fingers1 = detector.fingersUp(hand1)
        lenght, info, img  = detector.findDistance(lmList1[8], lmList1[12], img) # With draw
        #lenght, info = detector.findDistance(lmList1[8], lmList1[12]) # no draw


        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"] #list of 21 Landmarks points
            bbox2 = hand2["bbox"] # Bouding Box Info x,y,w,h
            centerpoint2 = hand2['center'] # center of the hand cx,cy
            handType2 = hand2["type"]# Hand type left or right

            fingers2 = detector.fingersUp(hand2)
            #lenght, info, img  = detector.findDistance(lmList1[8], lmList2[8], img) # With draw
            lenght, info, img  = detector.findDistance(centerpoint1, centerpoint2, img) # With draw


            #print(fingers1,fingers2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)