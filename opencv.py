import cv2 as cv2
import time
import numpy as np
import pandas as pd



img_resp = requests.get(url)
img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
imgOriginalScene = cv2.imdecode(img_arr, -1)

cv2.imshow("IPcamera", imgOriginalScene)
cv2.namedWindow('IPcamera', cv2.WINDOW_NORMAL)
cv2.resizeWindow('IPcamera', 300, 300)