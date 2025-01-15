import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

import os


cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1, detectionCon=0.7)  # Set detection confidence

offset = 20
imgSize = 300
folder = "Data/Z"
counter = 0

while True:
    success, img = cap.read()
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

        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap:hCal + hGap, :] = imgResize

        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)


    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord("s") and hands:
        counter += 1
        save_path = f'{folder}/Image_{time.time()}.jpg'
        cv2.imwrite(save_path, imgWhite)
        print(f"Image saved: {save_path} ({counter})")
