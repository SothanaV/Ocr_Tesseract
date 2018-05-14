import numpy as np
import cv2
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import time

cap = cv2.VideoCapture(0)

while(True):
    image = cap
    ret, frame = cap.read()
    text = pytesseract.image_to_string(frame)
    cv2.imshow('video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    print(text)
cap.release()
cv2.destroyAllWindows()
