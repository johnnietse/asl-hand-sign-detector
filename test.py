import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import time
import os


cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1, detectionCon=0.7)  # Set detection confidence
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

offset = 20
imgSize = 300
folder = "Data/Z"
counter = 0

labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

while True:
    success, img = cap.read()
    imgOutput = img.copy()
    if not success:
        print("Failed to capture video. Check the webcam connection.")
        break
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']


        # Ensure crop region is within image bounds
        y1 = max(0, y - offset)
        y2 = min(img.shape[0], y + h + offset)
        x1 = max(0, x - offset)
        x2 = min(img.shape[1], x + w + offset)

        imgCrop = img[y1:y2, x1:x2]

        # Validate imgCrop
        if imgCrop.size == 0:
            print("Invalid crop detected. Skipping frame.")
            continue

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255



        aspectRatio = h / w
        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap:wCal + wGap] = imgResize
            prediction, index = classifier.getPrediction(imgWhite,draw=False)
            print(prediction, index)

        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap:hCal + hGap, :] = imgResize
            prediction, index = classifier.getPrediction(imgWhite,draw=False)


        cv2.rectangle(imgOutput, (x - offset,y - offset-50),(x - offset+90,y - offset-50+50),(255,64,0),cv2.FILLED)

        cv2.putText(imgOutput,labels[index],(x,y-26),cv2.FONT_HERSHEY_COMPLEX,1.7,(255,255,255),2)
        cv2.rectangle(imgOutput, (x-offset,y-offset),(x + w+offset,y + h+offset),(255,64,0),4)


        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)


    cv2.imshow("Image", imgOutput)
    cv2.waitKey(1)

