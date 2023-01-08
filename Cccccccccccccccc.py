#0416
import cv2
src = cv2.imread('./sample/blackcat.jpg')

rows,cols,channels = src.shape
M1 = cv2.getRotationMatrix2D((rows/2, cols/2), 45, 0.5)  #영상의 중심인 center=(rows/2,cols/2)를 기준으로 scale=0.5로 축소하고, angle=45도(반시계방향)로 회전
M2 = cv2.getRotationMatrix2D((rows/2, cols/2), -45, 1.0)  #영상의 중심인 center=(rows/2,cols/2)를 기준으로 scale=1.0으로 확대 또는 축소를 하지 않고, angle=-45도(시계방향)으로 회전

dst1 = cv2.warpAffine(src, M1, (rows,cols))
dst2 = cv2.warpAffine(src, M2, (rows,cols))

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()