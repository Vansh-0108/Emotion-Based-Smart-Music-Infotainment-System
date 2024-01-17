from utils import predict
import numpy as np
import cv2 as cv

image = cv.VideoCapture(1)
ret, frame = image.read()
cv.imwrite("img.jpeg", frame)
image.release()
gray_image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) 
bigger = cv.resize(gray_image, (48, 48))
numpydata = np.asarray(bigger)
cv.imwrite("img2.jpeg", bigger)

predict(numpydata)