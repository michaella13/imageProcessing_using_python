import cv2

img=cv2.imread("lena.jpg")

img_edges=cv2.Canny(img, 100,200)

cv2.imshow('Image', img_edges)
#to save img
cv2.imwrite("edgesLena.jpg", img_edges)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()