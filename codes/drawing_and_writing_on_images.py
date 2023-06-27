import cv2 as cv
import numpy as np

# READING AND DISPLAYING AN IMAGE

Blue_S2000 = cv.imread("random_images\Blue_R34_GTR_From_The_Side.jpg")    # reads the image and stores it as a matrix

blankImage = np.zeros_like(Blue_S2000)  # generating the blank image

print("\n\nhere we go:\t" + str( blankImage.shape ))

blankImage[::3] = 0, 255, 255   # coloring the blank image

cv.rectangle(Blue_S2000, (40, 100, 320, 110), (0, 255, 0), 2)   # draw a rectangle

cv.circle(blankImage, (blankImage.shape[1]//2,blankImage.shape[0]//2), 100,(0, 255, 0), 2)  # draw a circle

cv.line(blankImage, (blankImage.shape[1]//1,blankImage.shape[0]//1), (blankImage.shape[1]//6,blankImage.shape[0]//6), (255, 0, 0), 5 )  # draw a line

cv.putText(Blue_S2000, "LIBERTY WALK", (blankImage.shape[1]//5,blankImage.shape[0]//5), cv.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 5)   # write text on a picture

cv.imshow("Blue_S2000", Blue_S2000)    # display the image

cv.imshow("blankImage", blankImage)    # display the image

cv.waitKey(10000)





