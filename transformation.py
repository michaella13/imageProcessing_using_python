import cv2
import numpy as np

# Create a VideoCapture object for the default camera (index 0)
live_stream = cv2.VideoCapture(0)

# Check if camera opened successfully
if not live_stream.isOpened():
    print("Error opening video stream or file")

# Set the frame width and height
live_stream.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
live_stream.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Read frames from the camera
while True:
    # Capture frame-by-frame
    ret, frame = live_stream.read()
    if ret:
        # Define kernel for morphological operations
        kernel = np.ones((5,5), np.uint8)

        # Apply dilation
        dilation = cv2.dilate(frame, kernel, iterations=1)
        # If the frame is returned, perform processing tasks on the frame
        # Display the frame
        cv2.imshow('Frame', dilation)
        # Wait for key press and exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture object and close all windows
live_stream.release()
cv2.destroyAllWindows()