import numpy as np
import cv2

img = cv2.imread("hehe.png")#we read the image
window_name = 'output'#window that opens when we click run is named as output
edged = cv2.Canny(img,100,200)#find the edges
#cv2.waitKey(0)
contours, hierarchy = cv2.findContours(edged,#img with edges
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)#retreives contours,approx contour
areas= []#will take all areas of rectangles

for x in contours:#for loop for filling areas array
        a= cv2.contourArea(x)#calc area of each rectangle
        areas.append(a)#appending to area
contours_sorted= sorted(contours, key=cv2.contourArea, reverse= True)#sorting the contours, true==largest to smallest
#cv2.imshow('Canny Edges After Contouring', edged)
#cv2.waitKey(0)
cv2.drawContours(img, contours_sorted[0], -1, (255, 128, 0), 3)#drawing the outline on largest rectangle
cv2.imshow('window_name', img)#displays the image which is now modified
#cv2.imshow("window_name",img)
#img = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, value=0)
cv2.waitKey(0)#python kernel might crash...waits for any key to be pressed
cv2.destroyAllWindows()#close all open windows
#contours is a numpy array with (x,y) as coordinates
#approx contour takes all coordinates of the rect into consideration(all the boundary)
