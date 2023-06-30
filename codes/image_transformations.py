import cv2 as cv
import numpy as np
import math

myImage = cv.resize(cv.imread("random_images\Honda_S2000_Blue.jpg"), (700, 700), interpolation=cv.INTER_CUBIC)  # get the image and rescale

cv.imshow("The Original Image", myImage)



# translation

# For info: https://www.geeksforgeeks.org/python-opencv-affine-transformation/

#To find the transformation matrix, we need three points from input image and 
# their corresponding locations in the output image
# Get 3 points from the original image as pts1 and give where will these 3 points be in the resulting matrix as pts2
pts1 = np.float32( [ [myImage.shape[0]//4, myImage.shape[0]//4], [myImage.shape[0]/2, myImage.shape[1]/2], [myImage.shape[0]/2, myImage.shape[0]/4] ] )

pts2 = np.float32( [ [myImage.shape[0],0], [myImage.shape[0]/2, myImage.shape[1]/2], [myImage.shape[0], myImage.shape[1]] ] )

M = cv.getAffineTransform(pts1, pts2)

transformedImage = cv.warpAffine(myImage, M, (myImage.shape[1], myImage.shape[0]) )

# cv.imshow("transformed image", transformedImage)

#   ROTATING AN IMAGE
def rotate_image(image, angle):
    #Source: https://stackoverflow.com/questions/9041681/opencv-python-rotate-image-by-x-degrees-around-specific-point
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv.getRotationMatrix2D(image_center, angle, 1.0)  
    result = cv.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv.INTER_LINEAR) # [1::-1] means starting from 1 to the start, by step size=-1 so inverting the shape tuple
    return result
# cv.imshow("rotated image", rotate_image(myImage, 45))


# FLIPPING THE IMAGE

flippedImage = cv.flip(myImage, flipCode=-1) # flipCode can be: 0, 1 or -1
# cv.imshow("FLIPPED IMAGE", flippedImage)

cv.waitKey(0)

