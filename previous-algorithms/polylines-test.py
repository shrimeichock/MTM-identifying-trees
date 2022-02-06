# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 14:23:04 2022

@author: user1

Sources:
    https://www.geeksforgeeks.org/python-opencv-cv2-polylines-method/?ref=lbp
    https://stackoverflow.com/questions/60051941/find-the-coordinates-in-an-image-where-a-specified-colour-is-detected
"""


# Python program to explain 
# cv2.polylines() method 
  
import cv2
import numpy as np
import matplotlib.pyplot as plt

  
# Reading an image in default
# mode
image = cv2.imread("test-images/skel-1.png")

# Window name in which image is
# displayed
window_name = 'Image'

white = [255,255,255]
# Get X and Y coordinates of all blue pixels
X,Y = np.where(np.all(image==white,axis=2))
print(X,Y, " Total:",len(X), len(Y))
zipped = np.column_stack((X,Y))
print(zipped)
 
# Polygon corner points coordinates
pts = np.array([[25, 20], [25, 100], 
                [200, 100], [200, 20]],
               np.int32)
  
pts = pts.reshape((-1, 1, 2))
  
isClosed = True
  
# Blue color in BGR
color = (255, 0, 0)
  
# Line thickness of 2 px
thickness = 1
  
# Using cv2.polylines() method
# Draw a Blue polygon with 
# thickness of 1 px
image = cv2.polylines(image, [pts], 
                      isClosed, color, thickness)




""" # DOES NOT WORK
pts = np.array(zipped)
pts = pts.reshape((-1, 1, 2))
  
isClosed = True
  
# Blue color in BGR
color = (255, 0, 0)
  
# Line thickness of 2 px
thickness = 1
  
# Using cv2.polylines() method
# Draw a Blue polygon with 
# thickness of 1 px
image = cv2.polylines(image, [pts], 
                      isClosed, color, thickness)"""
  


# Displaying the image
plt.figure()
plt.plot(), plt.imshow(image)
plt.title('Polygon image')
plt.xticks([]), plt.yticks([])
plt.show()
