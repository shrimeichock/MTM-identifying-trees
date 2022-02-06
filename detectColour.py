# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 13:57:53 2022
@author: user
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.png')

#plt.imshow(img)
grid_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

grid_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#plt.imshow(grid_HSV)

lower_color = np.array([40, 25,0]) 
upper_color = np.array([220, 225, 125])
mask = cv2.inRange(grid_HSV, lower_color, upper_color)

#define kernel size  
kernel = np.ones((7,7),np.uint8)
# Remove unnecessary noise from mask
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
#mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

edged = cv2.Canny(mask, 170,255)
contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
for cnt in contours:
    moment=cv2.moments(cnt) 
    #cx = int(moment['m10'] / moment['m00']) 
    #cy = int(moment['m01'] / moment['m00']) 
    #contoursNew, hierarchyNew = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img,[cnt],-1,(0,255,0),2)

#plt.imshow(img)


def grab_contours(cnts):
    # OpenCV v2.4, v4-official
    if len(cnts) == 2:
        return cnts[0]
    # OpenCV v3
    elif len(cnts) == 3:
        return cnts[1]
    
#filename = "test.png"
#cv2.imwrite(mask)

image = cv2.imread("test.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 120, 255, 1)
cv2.imshow("canny", edged)

cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
cnts = grab_contours(cnts)

contour_image = edged.copy()
area = 0

for c in cnts:
    area += cv2.contourArea(c) 
    cv2.drawContours(contour_image,[c], 0, (100,5,10), 3)

print(area)
cv2.putText(contour_image, str(area), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100,255,100), 2)
cv2.imshow("area", contour_image)
cv2.waitKey(0)

segmented_img = cv2.bitwise_and(img, img, mask=mask)


# Showing the output
#cv2.imshow("Output", output)

#plt.imshow(segmented_img)
plt.imshow(mask)

# cv2.imwrite('test-images/mask.png', mask)
