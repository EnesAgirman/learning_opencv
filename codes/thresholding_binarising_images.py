import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math

myImage = cv.imread("random_images\CAR_WITH_ARUCO_MARKERS.png")
myImage = cv.resize(myImage, ( myImage.shape[1]//2, myImage.shape[0]//2 ) )
cv.imshow("Original Image", myImage)

myImageGrayScaled = cv.cvtColor(myImage, cv.COLOR_BGR2GRAY)
# cv.imshow("GrayScale of the Original Image", myImageGrayScaled)


# Use cv.THRESH_BINARY_INV instead of cv.THRESH_BINARY to invert black and white
myThreshold, myTresholdedImage = cv.threshold(myImageGrayScaled, 155, 255, cv.THRESH_BINARY+cv.THRESH_OTSU) # Adding OTSU decreases the noise but prevents you from using your own threshold value
# cv.imshow("Thresholded Image", myTresholdedImage)

myImageWithAdaptiveThreshold = cv.adaptiveThreshold(myImageGrayScaled, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                          cv.THRESH_BINARY, blockSize=119, C=3) # Play with blockSize to get different results, ie. 11 gives drawing like image
# cv.imshow("Adaptive Thresholded Image", myImageWithAdaptiveThreshold)

myImageWithGaussianAdaptiveThreshold = cv.adaptiveThreshold(myImageGrayScaled, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                          cv.THRESH_BINARY_INV, blockSize=11, C=3) # gives similar but better results than cv.ADAPTIVE_THRESH_MEAN_C
# cv.imshow("Gaussian Adaptive Thresholded Image", myImageWithGaussianAdaptiveThreshold)
# Note: the blocksize can varry a lot. Some uses 199, some uses 11.

cv.waitKey(0)