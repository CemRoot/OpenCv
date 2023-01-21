import cv2
# Read image
# if you want to image to be in gray scale then use 0
img = cv2.imread('flower-image.jpg',0)
# Display image
cv2.imshow('image', img)
#to save image use cv2.imwrite('filename',img) when program is stopped code will save to gry scale image
cv2.imwrite('flower-image-gray.jpg',img)

# Wait for any key to be pressed
cv2.waitKey(0)
# Close all windows
cv2.destroyAllWindows()