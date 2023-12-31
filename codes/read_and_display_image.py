import cv2 as cv

# READING AND DISPLAYING AN IMAGE

Blue_S2000 = cv.imread('random_images\Honda_S2000_Blue.jpg')    # reads the image and stores it as a matrix

cv.imshow("CAR", Blue_S2000)    # display the image

cv.waitKey(10000)    # waits 3000 miliseconds for you to press any key, closes the window even if you haven't pressed after 3000 miliseconds

## cv.waitkey(10000) also returns the unicode of the pressed key in that time frame given to it(10000ms in this case) and returns -1 if no key is pressed