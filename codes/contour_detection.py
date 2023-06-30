import cv2 as cv
import numpy as np
import math

print("\n\n\nhehehehehehehehehehehehee boooooii\n\n")

myImage = cv.imread("random_images\CAR_WITH_ARUCO_MARKERS.png") # get the image
myImage = cv.resize(myImage, (myImage.shape[1]//2, myImage.shape[0]//2), interpolation=cv.INTER_CUBIC)  # rescale the image
cv.imshow("Myimage Original", myImage)

myImageGrayScale = cv.cvtColor(myImage, cv.COLOR_BGR2GRAY)  # convert to grayscale
cv.imshow("the grayscale image", myImageGrayScale)

""" 
myImageGrayScaleBlurred = cv.GaussianBlur(myImageGrayScale, (3, 3), cv.BORDER_DEFAULT)
cv.imshow("the blurred grayscale image", myImageGrayScaleBlurred)
"""

# definitely read this to understand cv2.Canny() : https://docs.opencv.org/3.4/d7/de1/tutorial_js_canny.html

ret, tresh = cv.threshold(myImageGrayScale, 190, 255, cv.THRESH_BINARY) # apply treshold

contoursTreshold, hierarchiesTreshold = cv.findContours( tresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE )  # find the contours

blankTreshold = np.zeros(myImage.shape, dtype='uint8')  # generate a blank image to draw the contours on

cv.drawContours(blankTreshold, contoursTreshold, -1, (0,255,0), 1)  # draw the contours

cv.imshow("Contours With Treshold", blankTreshold)  # display the contours


myImageCanny = cv.Canny(myImageGrayScale, 190, 200, apertureSize=3, L2gradient=True)    # apply canny edge detection
cv.imshow("Myimage Edges With Canny", myImageCanny)

contoursCanny, hierarchiesCanny = cv.findContours( myImageCanny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE ) # find the contours

# cv.imshow("tresh", tresh)

blankCanny = np.zeros(myImage.shape, dtype='uint8') # generate a blank image to draw the contours on

cv.drawContours(blankCanny, contoursCanny, -1, (0,255,0), 1)  # draw the contours

cv.imshow("Contours With Canny", blankCanny)  # display the contours

# print(f"\n{len(contours)} contours found\n")


cv.waitKey(0)
