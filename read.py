import cv2

img = cv2.imread('lena.jpg')

cv2.imshow('Image', img)
# Wait for key press and exit if 'q' is pressed
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()