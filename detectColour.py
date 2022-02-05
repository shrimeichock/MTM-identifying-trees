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

lower_color = np.array([45, 50, 0]) 
upper_color = np.array([220, 225, 125])
mask = cv2.inRange(grid_HSV, lower_color, upper_color)

#define kernel size  
kernel = np.ones((7,7),np.uint8)
# Remove unnecessary noise from mask
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
#mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

edged = cv2.Canny(mask, 170,255)
contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
output = cv2.drawContours(edged, contours, -1, (0, 0, 255), 3)




segmented_img = cv2.bitwise_and(img, img, mask=mask)


# Showing the output
#cv2.imshow("Output", output)

plt.imshow(segmented_img)
#plt.imshow(mask)