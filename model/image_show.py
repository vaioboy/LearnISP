from matplotlib import pyplot as plt
from matplotlib import image as img
import numpy as np
import cv2

#input is a RGB numpy array with shape (height,width,3), can be uint,int, float or double, values expected in the range 0..255
#output is a double YUV numpy array with shape (height,width,3), values in the range 0..255
def RGB2YUV( rgb ):
     
    m = np.array([[ 0.29900, -0.16874,  0.50000],
                 [0.58700, -0.33126, -0.41869],
                 [ 0.11400, 0.50000, -0.08131]])
     
    yuv = np.dot(rgb,m)
    yuv[:,:,1:]+=128.0
    return yuv

#input is an YUV numpy array with shape (height,width,3) can be uint,int, float or double,  values expected in the range 0..255
#output is a double RGB numpy array with shape (height,width,3), values in the range 0..255
def YUV2RGB( yuv ):
      
    m = np.array([[ 1.0, 1.0, 1.0],
                 [-0.000007154783816076815, -0.3441331386566162, 1.7720025777816772],
                 [ 1.4019975662231445, -0.7141380310058594 , 0.00001542569043522235] ])
    
    rgb = np.dot(yuv,m)
    rgb[:,:,0]-=179.45477266423404
    rgb[:,:,1]+=135.45870971679688
    rgb[:,:,2]-=226.8183044444304
    return rgb

image = img.imread('../image/Scrat_640x480.jpg')

image_yuv = RGB2YUV(image).astype(int)

image_rgb = YUV2RGB(image).astype(int)

plt.subplot(1,3,1)
plt.imshow(image)

plt.subplot(1,3,2)
plt.imshow(image_yuv)

plt.subplot(1,3,3)
plt.imshow(image_rgb)

plt.show()

cv_image = cv2.imread('../image/Scrat_640x480.jpg')
cv2.imwrite('Scrat.jpg', cv_image)