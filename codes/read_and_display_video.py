import cv2 as cv

def rescaleFrame(myFrame, myScale): # function for rescaling images
    
    myHeight = int(myFrame.shape[0] * myScale)
    myWidth = int(myFrame.shape[1] * myScale)
    
    dimensions = (myHeight, myWidth)
    
    result = cv.resize(myFrame, dimensions, interpolation=cv.INTER_AREA)
    
    return result


myVideoCapture = cv.VideoCapture("random_videos\You're God damn right..mp4")

while cv.waitKey(20) & 0xFF != ord(" "):
    theVideoIsRead, currentFrame = myVideoCapture.read()
    
    if theVideoIsRead == True:
        # currentFrame = cv.cvtColor(currentFrame, cv.COLOR_BGR2GRAY)    # converting the frame to grayscale
        currentFrame = cv.GaussianBlur(currentFrame, (11, 11), cv.BORDER_DEFAULT) # adding blur
        currentFrame = cv.Canny(currentFrame, 100, 200, apertureSize=5)   #edge detection
        cv.imshow("Press space to close", currentFrame)
    
myVideoCapture.release()

cv.destroyAllWindows()
cv.waitKey(0)

# Go look at this link for explanation of the if condition:
# https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1#:~:text=The%20waitKey(0)%20function%20returns,waitKey(0)%20to%200xFF%20.










