#0422
import cv2
import numpy as np
import time

dst = np.full((512,512,3), (255,255,255), dtype = np.uint8)
nPoints = 100
pts = np.zeros((1, nPoints, 2), dtype = np.uint16)

cv2.setRNGSeed(int(time.time()))  #난수 생성을 초기화, 초기화하지 않으면 항상 같은 난수열을 생성
cv2.randn(pts,mean = (256,256), stddev = (50,50))  #1xnPoints이고 2-채널인 pts 배열에 mean=(256,256), stddev=(50,50)인 정규분포 난수 생성

#draw points
for k in range(nPoints):
    x,y = pts[0][k,:]    #pts[0,k,:]  #ptspts[0,k]의 채널 데이터를 x,y에 저장
    cv2.circle(dst, (x,y), radius = 5, color=(0,0,255), thickness = -1)

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()