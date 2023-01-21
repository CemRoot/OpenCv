# Import
import cv2
import numpy as np


# Read image
# if you want to image to be in gray scale then use 0
img = cv2.imread('flower-image.jpg')
# img.item gives the value of pixel at (x,y) coordinate in the image and 0 = blue, 1 = green, 2 = red
print(str(img.item(100,100,2)))
# setting the value of pixel at (x,y) coordinate in the image and 0 = blue, 1 = green, 2 = red
img.itemset((100,100,2),255)
# size of image in pixels
print("pikxel sayısı:",img.size)

#shape gives the number of rows, columns and channels (if image is color)
print(img.shape)

# Display image
cv2.imshow('image', img)
#to save image use cv2.imwrite('filename',img) when program is stopped code will save to gry scale image
cv2.imwrite('flower-image-gray.jpg',img)


# ROI = Region of Image SYNTAX: img[y:y+h, x:x+w]
ROI = img[100:200, 100:200]
cv2.imshow('ROI', ROI)

#b g r değerlerini değiştirme
img = cv2.imread('flower-image.jpg')
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))
cv2.imshow('image', img)



# Wait for any key to be pressed
cv2.waitKey(0)
# Close all windows
cv2.destroyAllWindows()