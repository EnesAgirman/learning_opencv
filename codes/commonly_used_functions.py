import numpy as np
import cv2 as cv

def rescaleFrame(myFrame, myScale): # function for rescaling images
    
    myHeight = int(myFrame.shape[0] * myScale)
    myWidth = int(myFrame.shape[1] * myScale)
    
    dimensions = (myHeight, myWidth)
    
    result = cv.resize(myFrame, dimensions, interpolation=cv.INTER_AREA)
    
    return result

myImage = rescaleFrame( cv.imread("random_images\Honda_S2000_Blue.jpg"), 0.7 )  # get the image and rescale

cv.imshow("Original Image", myImage)    # displaying the image


grayScaleImage = cv.cvtColor(myImage, cv.COLOR_BGR2GRAY)    # converting the image to grayscale

# cv.imshow("GrayScale Image", grayScaleImage)    # displaying the GrayScale image

# You can watch this to understand how blurring works: https://www.youtube.com/watch?v=C_zFhWdM4ic&ab_channel=Computerphile
blurredImage = cv.blur(myImage, (3, 3), cv.BORDER_DEFAULT)  # I think cv.blur() uses mean blur
# cv.imshow("Blurred Image(Mean)", blurredImage)
blurredImage = cv.GaussianBlur(myImage, (3,3), cv.BORDER_DEFAULT)   # this is the gaussian blur, prefer this for edge detection problems
# cv.imshow("Blurred Image(Gaussian)", blurredImage)


cv.waitKey(10000)



