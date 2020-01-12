import numpy as np
import cv2

rgb = cv2.cvtColor(cv2.imread('data/depth_0_057660.png'), cv2.COLOR_BGR2RGB)
print(rgb.shape, rgb.dtype, rgb.ndim)

#normalized = (R + G * 256 + B * 256 * 256) / (256 * 256 * 256 - 1)
#in_meters = 1000 * normalized
a = np.array([1000/(256 * 256 * 256 - 1), 256*1000/((256 * 256 * 256 - 1)), 256*256*1000/(256 * 256 * 256 - 1)], dtype=np.float32)

grayscale = rgb @ a
print(grayscale.shape, grayscale.dtype, grayscale.ndim)

print(grayscale[599,799])

cv2.imwrite("data/depth_0_057660.exr", grayscale);
print("write data/depth_0_057660.exr")
