#0426
import cv2
import numpy as np

src = cv2.imread('./sample/browncat.jpg')
b,g,r = cv2.split(src)  #영상을 컬러로 읽은 src를 b,g,r에 채널 분리
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)

X = src.reshape(-1,3)  #src.reshape(-1,3)으로 모양을 재조정하여 X의 각 행에 화소의 컬러값을 위치시킨다.
print('X.shape = ', X.shape)

mean,eVects = cv2.PCACompute(X, mean = None)  #X의 평균 벡터 mean, 공분산 행렬의 고유 벡터 eVects를 계산. eVects는 3x3 행렬
print('mean = ', mean)
print('eVects = ', eVects)

Y = cv2.PCAProject(X,mean,eVects)  #cv2.PCAProject() 함수로 고유 벡터 eVects에 의해 X를 Y에 PCA 투영
Y = Y.reshape(src.shape)  #Y의 모양을 src 모양으로 재조정한다.
print('Y.shape = ', Y.shape)

eImage = list(cv2.split(Y))  #Y를 eImage에 채널 분리하고, cv2.normalize()로 각 채널 eImage[i]의 값을 [0,255]로 정규화하여 eImage[i].astype(np.uint8)으로 8-비트 영상으로 변환
for i in range(3) :
    cv2.normalize(eImage[i], eImage[i], 0, 255, cv2.NORM_MINMAX)
    eImage[i] = eImage[i].astype(np.uint8)

cv2.imshow('eImage[0]', eImage[0])
cv2.imshow('eImage[1]', eImage[1])
cv2.imshow('eImage[2]', eImage[2])
cv2.waitKey()
cv2.destroyAllWindows()