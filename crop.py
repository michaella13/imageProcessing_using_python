import cv2
#0 indicating this webcam, current
live_stream=cv2.VideoCapture(0)

if not live_stream.isOpened():
    print("Error opening the webcam")

#setting the video frame size
live_stream.set(cv2.CAP_PROP_FRAME_WIDTH,640)
live_stream.set(cv2.CAP_PROP_FRAME_HEIGHT,400)

while True:
    ret,frame=live_stream.read()
    if ret:
        x, y, width, height = 100, 100, 200, 200
        cv2.imshow("myself",frame[y:y+height,x:x+height])
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

#clean memory
live_stream.release()
cv2.destroyAllWindows()
        