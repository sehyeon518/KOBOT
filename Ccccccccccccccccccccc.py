#0421
import cv2
import numpy as np
import time

dst = np.full((512,512,3), (255,255,255), dtype = np.uint8)
nPoints = 100
pts = np.zeros((1,nPoints,2), dtype = np.uint16)
 #난수 생성 초기화, 초기화하지 않으면 항상 같은 난수열을 생성하므로 주의
cv2.randu(pts, (0,0), (512,512))  #1xnPoints이고 2-채널인 pts 배열에 (0,0)에서 (512,512) 범위의 균등분포 난수를 생성

#draw points
for k in range(nPoints):
    x,y = pts[0,k][:]     #pts[0,k,:]  #ptspts[0,k]의 채널 데이터를 x,y에 저장
    cv2.circle(dst, (x,y), radius = 5, color = (0,0,255), thickness = -1)  #cv2.circle() 함수로 좌표 (x,y)에 반지름 5이고 컬러(0,0,255)인 원을 dst에 표시

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()