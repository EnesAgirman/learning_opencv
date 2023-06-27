import cv2 as cv
import numpy as np


Blue_S2000 = cv.imread('random_images\Honda_S2000_Blue.jpg')    # reads the image and stores it as a matrix
# print("it is: " + str(Blue_S2000.shape))



def rescaleFrame(myFrame, myScale):
    
    myHeight = int(myFrame.shape[0] * myScale)
    myWidth = int(myFrame.shape[1] * myScale)
    
    dimensions = (myHeight, myWidth)
    
    result = cv.resize(myFrame, dimensions, interpolation=cv.INTER_AREA)
    
    return result


rescaled_Blue_S2000 = rescaleFrame(Blue_S2000, 0.5)

cv.imshow("myImage", Blue_S2000)
cv.imshow("myImage_rescaled", rescaled_Blue_S2000)
    
cv.waitKey(10000)





