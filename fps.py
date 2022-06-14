import cv2
import time

cap= cv2.VideoCapture('data\camera.mp4')
framespersecond= int(cap.get(cv2.CAP_PROP_FPS))
print("The total number of frames in this video is ", framespersecond) #The total number of frames in this video is  15