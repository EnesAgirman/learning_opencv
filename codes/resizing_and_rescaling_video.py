import cv2 as cv

def rescaleFrame(myFrame, myScale):
    
    myHeight = int(myFrame.shape[0] * myScale)
    myWidth = int(myFrame.shape[1] * myScale)
    
    dimensions = (myWidth, myHeight)
    
    result = cv.resize(myFrame, dimensions, interpolation=cv.INTER_AREA)
    
    return result


myVideoCapture = cv.VideoCapture("random_videos\You're God damn right..mp4")

while cv.waitKey(20) & 0xFF != ord(" "):
    theVideoIsReady, currentFrame =  myVideoCapture.read()
    
    if theVideoIsReady == True:
        cv.imshow("Press space to close", currentFrame)
        cv.imshow("Also press space to close", rescaleFrame(currentFrame, 0.4))

    
myVideoCapture.release()

cv.destroyAllWindows()
cv.waitKey(100)

