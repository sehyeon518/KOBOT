import cv2
import numpy as np

scr1 = cv2.imread('./sample/browncat.jpg', cv2.IMREAD_GRAYSCALE)
scr2 = np.zeros(shape = (408,340), dtype = np.uint8) + 100

dst1 = scr1 + scr2
dst2 = cv2.add(scr1,scr2)
#dst2 = cv2.add(src1,src2,dtype = cv2.CV_8U)

cv2.imshow('dst1',dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()