import cv2

img=cv2.imread("lena.jpg")

gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Image', gray_img)
#to save img
cv2.imwrite("grayLena.jpg", gray_img)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()