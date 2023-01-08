import cv2
##import numpy as  np

img = cv2.imread("./sample/browncat.jpg", cv2.IMREAD_GRAYSCALE)
print('img.shape = ', img.shape)

## img = img.reshape(img.shape[0] * img.shape[1])
img = img.flatten() #다차원 배열을 1차원 배열로 변경하여 img.sape = (138720,)
print('img.shape = ', img.shape)

img = img.reshape(-1, 408, 340) #3차원 배열로 확장. -1로 표시된 부분은 크기를 자동으로 계산. reshape는 실제 데이터를 변경하지는 않고, 모양을 변경함
print('img.shape = ', img.shape)

cv2.imshow('img', img[0]) #그레이스케일 영상을 화면에 표시
cv2.waitKey()
cv2.destroyAllWindows()

#영상의 확대 축소 크기는 cv2.resize()로 변환한다