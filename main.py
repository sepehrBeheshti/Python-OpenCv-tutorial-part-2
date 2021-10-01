from cv2 import *
import cv2
import keyboard
import numpy as np

video = VideoCapture(0)
while True:
    nothing, img = video.read()
    imgResized = cv2.resize(img, (0, 0), fx=.5, fy=.5)
    blue, green, red = cv2.split(imgResized)
    zero_channel = np.zeros(imgResized.shape[:2], dtype="uint8")
    blue_img = cv2.merge([blue, zero_channel, red])
    cv2.imshow("Webcam", blue_img)
    cv2.waitKey(1)
    if keyboard.is_pressed("q"):
        quit()
