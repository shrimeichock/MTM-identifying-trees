# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 13:57:53 2022
@author: user
Source: https://techvidvan.com/tutorials/detect-objects-of-similar-color-using-opencv-in-python/ 
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

ACRES_IN_PLOT = 64

img = cv2.imread('LotsOFTrees.png') #must be png

#plt.imshow(img)
#grid_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

grid_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#plt.imshow(grid_HSV)

lower_color = np.array([40, 20, 0]) #increase H if more green in the picture
upper_color = np.array([220, 225, 125]) #HueSaturationValue
mask = cv2.inRange(grid_HSV, lower_color, upper_color)

#define kernel size  
kernel = np.ones((7,7),np.uint8)
# Remove unnecessary noise from mask
#mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
#mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

#edged = cv2.Canny(mask, 170,255)
contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#output = cv2.drawContours(edged, contours, -1, (0, 0, 255), 3)

tree_area = 0
height, width, channels = img.shape
print(f"Size of image in pixels: {height} x {width}")
total_area_plot = height*width
hectare_size = total_area_plot/ACRES_IN_PLOT #area in pixels of 1 hectare

for cnt in contours:
    if cv2.contourArea(cnt) < hectare_size: #replace with # pixels for 1 hectare
        tree_area += cv2.contourArea(cnt)
        cv2.drawContours(img,[cnt],-1,(0,255,0),2) #outline in green
    else:
        cv2.drawContours(img,[cnt],-1,(200,0,0),2) #outline in red

print("Area of trees in pixels:", tree_area) 
percentage = tree_area/total_area_plot
print("Percentage of area covered by trees:",round(percentage*100,2), "%") 

plt.imshow(img) #show green image

#plt.imshow(mask) #show purple image

# cv2.imwrite('test-images/mask.png', mask)
