# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 13:57:53 2022
@author: user
Source: https://techvidvan.com/tutorials/detect-objects-of-similar-color-using-opencv-in-python/ 
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.png')

#plt.imshow(img)
grid_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

grid_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#plt.imshow(grid_HSV)

lower_color = np.array([50, 20, 0]) #increase H if more green in the picture
upper_color = np.array([220, 225, 125]) #HueSaturationValue
mask = cv2.inRange(grid_HSV, lower_color, upper_color)

#define kernel size  
kernel = np.ones((7,7),np.uint8)
# Remove unnecessary noise from mask
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
#mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

edged = cv2.Canny(mask, 170,255)
contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#output = cv2.drawContours(edged, contours, -1, (0, 0, 255), 3)

for cnt in contours:
    moment=cv2.moments(cnt) 
    cv2.drawContours(img,[cnt],-1,(0,255,0),2)

plt.imshow(img) #show green image

segmented_img = cv2.bitwise_and(img, img, mask=mask)


# Showing the output
#cv2.imshow("Output", output)

#plt.imshow(segmented_img)
#plt.imshow(mask) #show purple image

# cv2.imwrite('test-images/mask.png', mask)
