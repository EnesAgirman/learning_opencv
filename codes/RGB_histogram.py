import cv2 as cv
import numpy as np
import math
import matplotlib.pyplot as plt


myImage = cv.imread("random_images\cats.jpg") # get the image
cv.imshow("Myimage Original", myImage)

blankImage = np.zeros_like(cv.cvtColor(myImage, cv.COLOR_BGR2GRAY))
myMask = cv.circle(blankImage, (myImage.shape[1]//2,myImage.shape[0]//2), 100, 255, -1)
cv.imshow("my mask", myMask)

myColors = ['b', 'g', 'r']

plt.figure(0)
plt.title("My Image RGB Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of Pixels")

for i, col in enumerate(myColors):
    print(str(i) + " " + col)
    myHist = cv.calcHist( [myImage], [i], myMask, [256], [0, 256] ) # put None instead of myMask to calculate the histogram for the full image
    plt.plot(myHist, color=col)
    plt.xlim( [0, 256] )

plt.show()
cv.waitKey(0)
