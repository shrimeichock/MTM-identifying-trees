# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 13:57:53 2022
@authors: Shrimei Chock, Maisha Abdullah, Thanuja Sivaanathan
Source: https://techvidvan.com/tutorials/detect-objects-of-similar-color-using-opencv-in-python/ 
Source: https://stackoverflow.com/questions/55544388/how-can-i-calculate-the-area-inside-non-contiguous-shapes-in-an-image
Source: https://stackoverflow.com/questions/46491643/find-area-of-cv2-findcontours-python-opencv?fbclid=IwAR33h-jPe5MAaAGe53r7rbYjJ_aAHSTmwvkWlVz0g6va7_xqN9Dwe5YtYWY
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

HECTARES_IN_PLOT = 64

img = cv2.imread('image2.png') #must be png

grid_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_color = np.array([40, 20, 0]) #increase H if more green in the picture
upper_color = np.array([220, 225, 125]) #HueSaturationValue
mask = cv2.inRange(grid_HSV, lower_color, upper_color)

#define kernel size  
kernel = np.ones((7,7),np.uint8)

contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

tree_area = 0
height, width, channels = img.shape
print(f"Size of image in pixels: {height} x {width}")
total_area_plot = height*width
hectare_size = total_area_plot/HECTARES_IN_PLOT #area in pixels of 1 hectare

for cnt in contours:
    if cv2.contourArea(cnt) < hectare_size: #replace with # pixels for 1 hectare
        tree_area += cv2.contourArea(cnt)
        cv2.drawContours(img,[cnt],-1,(0,255,0),2) #outline in green
    else:
        cv2.drawContours(img,[cnt],-1,(200,0,0),2) #outline in red

print("Area of trees in pixels:", tree_area)
percentage = tree_area/total_area_plot
print("Area of trees in hectares:", tree_area/hectare_size)
print("Percentage of area covered by trees:",round(percentage*100,2), "%") 

plt.imshow(img) #show green image
