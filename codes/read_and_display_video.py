import cv2 as cv


myVideoCapture = cv.VideoCapture("random_videos\You're God damn right..mp4")

while cv.waitKey(20) & 0xFF != ord("s"):
    theVideoIsRead, currentFrame =  myVideoCapture.read()
    
    if theVideoIsRead == True:
        cv.imshow("myVideo", currentFrame)
    
myVideoCapture.release()

cv.destroyAllWindows()
cv.waitKey(100)

# Go look at this link for explanation of the if condition:
# https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1#:~:text=The%20waitKey(0)%20function%20returns,waitKey(0)%20to%200xFF%20.










