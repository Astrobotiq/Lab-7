import cv2
import numpy as np

img=cv2.imread("Screenshot (292).png")

blue,green,red = cv2.split(img)

zeros = np.zeros(blue.shape,np.uint8)

blueBGR = cv2.merge([blue,zeros,zeros])
greenBGR = cv2.merge([zeros,green,zeros])
redBGR = cv2.merge([zeros,zeros,red])
blueRedImage = cv2.merge([blue,zeros,red])
finalImage = cv2.merge([blue,green,red])

cv2.imshow('Blue Channel', blueBGR)
cv2.waitKey(0)
cv2.imshow('Green Channel', greenBGR)
cv2.waitKey(0)
cv2.imshow('Red Channel', redBGR)
cv2.waitKey(0)
cv2.imshow('Blue+Green', blueRedImage)
cv2.waitKey(0)
cv2.imshow('Final Image', finalImage)
cv2.waitKey(0)




cv2.destroyAllWindows()
