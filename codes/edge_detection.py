import math as math
import cv2 as cv
import numpy as np


def rescaleFrame(myFrame, myScale): # function for rescaling images
    
    myHeight = int(myFrame.shape[0] * myScale)
    myWidth = int(myFrame.shape[1] * myScale)
    
    dimensions = (myHeight, myWidth)
    
    result = cv.resize(myFrame, dimensions, interpolation=cv.INTER_AREA)
    
    return result

def kernelConvolution2D(matrix2D, aKernel):
    
    result = np.zeros_like(matrix2D)
    
    for i in range(1, matrix2D.shape[0]-1):
        for j in range(1, matrix2D.shape[1]-1):    
            Sum = 0

            Sum += matrix2D[i-1, j-1] * aKernel[0, 0]
            Sum += matrix2D[i-1, j] * aKernel[0, 1]
            Sum += matrix2D[i-1, j+1] * aKernel[0, 2]
            
            Sum += matrix2D[i, j-1] * aKernel[1, 0]
            Sum += matrix2D[i, j] * aKernel[1, 1]
            Sum += matrix2D[i, j+1] * aKernel[1, 2]
            
            Sum += matrix2D[i+1, j-1] * aKernel[2, 0]
            Sum += matrix2D[i+1, j] * aKernel[2, 1]
            Sum += matrix2D[i+1, j+1] * aKernel[2, 2]
            
            result[i, j] = Sum // 9
    return result

Gx = np.array( [ [-1, 0, 1], [-2, 0, 2], [-1, 0, 1] ] )

Gy = np.array( [ [-1, -2, -1], [0, 0, 0], [1, 2, 1] ] )

myImage = rescaleFrame( cv.imread("random_images\Honda_S2000_Blue.jpg"), 0.7 )  # get the image and rescale
cv.imshow("Original Image", myImage)    # displaying the image

grayScaleImage = cv.cvtColor(myImage, cv.COLOR_BGR2GRAY)    #convertion to grayscale

hori = kernelConvolution2D(grayScaleImage, Gx)
vert = kernelConvolution2D(grayScaleImage, Gy)

cv.imshow("Myimage horizontal", hori)
cv.imshow("Myimage vertical", vert)

MyImageResult = np.zeros_like(grayScaleImage)
for i in range(1, MyImageResult.shape[0]):
    for j in range(1, MyImageResult.shape[1]):
        MyImageResult[i, j] = math.sqrt(math.pow(hori[i, j], 2) + math.pow(vert[i, j], 2))

 
cv.imshow("Myimage Average", cv.Canny(myImage, 100, 200))

cv.waitKey(0)

