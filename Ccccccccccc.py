#0411
import cv2
src = cv2.imread('./sample/browncat.jpg')

dst = cv2.split(src)
print(type(dst))
print(type(dst[0]))  #type(dst[1]), type(dst[2])

cv2.imshow('blue', dst[0])
cv2.imshow('greed', dst[1])
cv2.imshow('red', dst[2])
cv2.waitKey()
cv2.destroyAllWindows()