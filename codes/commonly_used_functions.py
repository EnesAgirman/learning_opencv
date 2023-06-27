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

cv.imshow("GrayScale Image", grayScaleImage)    # displaying the GrayScale image

cv.waitKey(10000)
