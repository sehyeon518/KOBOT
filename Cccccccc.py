#0408
import cv2

src = cv2.imread('./sample/graycat.jpg', cv2.IMREAD_GRAYSCALE)
rects = cv2.selectROIs('src',src,False,True)  #'src' 윈도우에 src 영상을 표시하고, showCrosshair = Fals로 서낵영역에 격자를 표시하지 않고 fromCenter = True로 마우스 클릭 위치 중심을 기준으로 드래그하여 박스를 선탣하고, 스페이스바/엔터키를 눌러 반복적으로 ROI 영역을 지정하고, Esc 키를 눌러 다중 영영 선택을 종료하면 rects에 반환
print('rects = ', rects)

for r in rects :
    cv2.rectangle(src, (r[0],r[1]), (r[0]+r[2],r[1]+r[3]),255)
##  img = src[r[1]:r[1]+r[3],r[0]:r[0]+r[2]]
##  cv2.imshow('Img',img)
##  cv2.waiKey()

cv2.imshow('src',src)
cv2.waitKey()
cv2.destroyAllWindows()