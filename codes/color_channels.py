import cv2 as cv
import numpy as np
import math

print("\n\n\nhihihihihihihihihihihihihihihihihihihihihi\n\n\n")

myImage = cv.imread("random_images\CAR_WITH_ARUCO_MARKERS.png") # get the image
myImage = cv.resize(myImage, (myImage.shape[1]//2, myImage.shape[0]//2), interpolation=cv.INTER_CUBIC)  # rescale the image
cv.imshow("Myimage Original", myImage)

grayScale = cv.cvtColor(myImage, cv.COLOR_BGR2GRAY)
cv.imshow("grayscale", grayScale)

coloredBack = cv.cvtColor(grayScale, cv.COLOR_GRAY2BGR)
cv.imshow("coloredBack", coloredBack)

print(f"{coloredBack[0:3:2]},\nand now\n {grayScale[0:3]}\n\n")

cv.waitKey(0)


