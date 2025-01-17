import cv2
import cvzone


# Start capturing video from camera index 1
cap = cv2.VideoCapture(0)
detector = cvzone.HandDetector(maxHands=1, detectionCon=1)
mySerial = cvzone.SerialObject("COM6", 9600, 1)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    if lmList:
        fingers = detector.fingersUp()
        mySerial.sendData(fingers)
    # Display the processed image with detected hands
    cv2.imshow("Image", img)

    # Check for key press events
    cv2.waitKey(1)
    