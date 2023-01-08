#0410
import cv2
import numpy as np

src = cv2.imread('./sample/blackcat.jpg', cv2.IMREAD_GRAYSCALE)
shape = src.shape[0], src.shape[1], 3
dst = np.zeros(shape, dtype = np.uint8)  #src와 같은 가로, 세로 크기의 3-채널 컬러 영상 dst를 생성

dst[:,:,0] = src  #B-채널  #dst의 0-채널(blue)에 src를 복사
##dst[:,:,1] = src  #G-채널
##dst[:,:,2] = src  #R-채널

dst[100:400, 200:300, :] = [255,255,255]

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()