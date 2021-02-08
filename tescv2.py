import cv2
import numpy as np

# img = np.zeros([512, 512, 3],np.uint8)
# a = np.array([(375, 193), (364, 113), (277, 20)])
# cv2.drawContours(img, [a], 0, (255,255,255), 2)
# cv2.imshow("line",img)
# cv2.waitKey()
font_size = cv2.getTextSize("gggYGK",cv2.FONT_HERSHEY_DUPLEX,1.0,5)
print(font_size)