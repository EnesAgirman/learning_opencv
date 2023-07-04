import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math

# Reading and scaling the image
# myImage = cv.imread( "random_images\CAR_WITH_ARUCO_MARKERS.png" )
# myImage = cv.resize(myImage, (myImage.shape[1]//2, myImage.shape[0]//2) )
# cv.imshow("the original image", myImage)

myImage = cv.imread( "random_images\Colorfull_Scenary.jpg" )
cv.imshow("the original image", myImage)

# Grayscale the image
myImageGrayScaled = cv.cvtColor(myImage, cv.COLOR_BGR2GRAY)
cv.imshow("grayscaled image", myImageGrayScaled)

## LAPLACIAN

# For Info: https://docs.opencv.org/3.4/d5/db5/tutorial_laplace_operator.html

# Generate the laplacian and scale it  and take the absolute
myImageLaplacianNonScaled = cv.Laplacian(myImageGrayScaled, cv.CV_16S, ksize=3)
myImageLaplacianScaled = cv.convertScaleAbs(myImageLaplacianNonScaled)

# Display the output
# cv.imshow("laplacian", myImageLaplacianScaled)



## SOBEL

# For info: https://docs.opencv.org/3.4/d2/d2c/tutorial_sobel_derivatives.html
# Calculate the X gradient
myGradX = cv.Sobel(myImageGrayScaled, cv.CV_64F, 1, 0, ksize=3, scale=1, delta=0, borderType=cv.BORDER_DEFAULT)
# You have to scale the gradient using the line of code below if you use ddepth=cv.CV_16S instead of cv.CV_64F
# myGradX = cv.convertScaleAbs(myGradX)
cv.imshow("X Gradient", myGradX)

# Calculate the Y gradient
myGradY = cv.Sobel(myImageGrayScaled, cv.CV_64F, 1, 0, ksize=3, scale=1, delta=0, borderType=cv.BORDER_DEFAULT)
# You have to scale the gradient using the line of code below if you use ddepth=cv.CV_16S instead of cv.CV_64F
# myGradY = cv.convertScaleAbs(myGradY)
cv.imshow("Y Gradient", myGradY)

# Combine the gradients
myGradsCombined = cv.bitwise_or(myGradX, myGradY)

# display the results
cv.imshow("My Grads Combined", myGradsCombined)

cv.waitKey(0)





