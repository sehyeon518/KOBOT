import cv2
import numpy as np

img = cv2.imread("./sample/browncat.jpg")   #cv2.IMREAD_COLOR
##img = cv2.imread("./sample/brow2ncat.jpg", cv2.IMREAD_GRAYSCALE)

print('img.ndim = ', img.ndim)
print('img.shape = ', img.shape)
print('img.dtype = ', img.dtype)

## np.bool, np.uint16, np.uint32, np.float32, np.float64, np.complex64
img = img.astype(np.int32)
print('img.dtype = ', img.dtype)

img = np.uint8(img)
print('img.dtype = ', img.dtype)