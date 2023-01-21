import cv2
import numpy as np
from matplotlib import pyplot as plt
# Read image
mavi=[255,0,0]
# imread() fonksiyonu ile resmi okuyoruz.
img=cv2.imread('flower-image.jpg')
# copyMakeBorder() fonksiyonu ile resmin kenarlarına 10 piksellik siyah bir çerçeve ekliyoruz.
replicate=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)
#cv2.BORDER_REPLICATE: kenar değerlerini tekrar ederek çerçeve oluşturur.
reflect=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)
reflect101=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT101)
wrap=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP)
constant=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=mavi)
# subplot() fonksiyonu ile resimleri gösteriyoruz. 231: 2 satır 3 sütun 1. resim
plt.subplot(231),plt.imshow(img,'gray'),plt.title('orjinal')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('replicate')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('reflect')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('reflect101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('wrap')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('constant')
# gösterilen resimleri kaydediyoruz.
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
