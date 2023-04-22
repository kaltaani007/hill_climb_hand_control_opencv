import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui


detector = HandDetector(detectionCon=0.5 , maxHands= 2)
cap = cv2.VideoCapture(0)
cap.set(3 , 600 )
cap.set(4 , 400)
while True :
    _, frame = cap.read()

    frame = cv2.flip(frame , 1)

    hand , frame = detector.findHands(frame)

    if hand and hand[0]["type"] == "Left":
        fingers = detector.fingersUp(hand[0])
        tot_fingers = fingers.count(1)
        cv2.putText (frame , f'total fings up {tot_fingers}' , (50 , 50 ), cv2.FONT_HERSHEY_PLAIN , 3, (0 , 255, 0 ))

        if tot_fingers == 5:
            pyautogui.keyDown("right")
            pyautogui.keyUp("left")

        if tot_fingers == 0:
            pyautogui.keyDown("left")
            pyautogui.keyUp("right")


    cv2.imshow("Frame Window" , frame)



    cv2.waitKey(1)


cv2.destroyAllWindows()