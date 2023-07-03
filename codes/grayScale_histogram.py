import cv2 as cv
import numpy as np
import math
import matplotlib.pyplot as plt


myImage = cv.imread("random_images\CAR_WITH_ARUCO_MARKERS.png") # get the image
myImage = cv.resize(myImage, (myImage.shape[1]//2, myImage.shape[0]//2), interpolation=cv.INTER_CUBIC)  # rescale the image
myImageGrayScaled = cv.cvtColor(myImage, cv.COLOR_BGR2GRAY)
cv.imshow("Myimage GrayScaled", myImageGrayScaled)

blankImage = np.zeros_like(myImageGrayScaled)
myMask = cv.rectangle( blankImage, (160, 310), (300, 460), 255, -1 )
# myMask = cv.rectangle( blankImage, (300, 300), (500, 460), 255, -1 )
cv.imshow("my mask", myMask)

myImageMasked = cv.bitwise_and(myImageGrayScaled, myImageGrayScaled, mask=myMask)
cv.imshow("masked image", myImageMasked)

myImageMaskedHistogram = cv.calcHist([myImageGrayScaled], [0], myMask, [256], [0, 256] )

plt.figure(0)
plt.title("My Image GrayScale Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of Pixels")
plt.plot(myImageMaskedHistogram)
plt.show()


cv.waitKey(0)

