import cv2
import numpy as np
import os

def partA():
    videoPath = "../Videos/RoseBloom.mp4"
    imgPath = "../Generated/frame_as_6.jpg"
    generatedPath = '../Generated/'
    
    cap = cv2.VideoCapture(videoPath)
    if (cap.isOpened()== False): 
        print('Error opening video stream')
    fps = cap.get(cv2.CAP_PROP_FPS)
    pos = fps * 5
    cap.set(cv2.CAP_PROP_POS_FRAMES, pos)
    _, frame = cap.read()
    cv2.imwrite(imgPath, frame)


def partB():
    imgPath = "../Generated/frame_as_6.jpg"
    genPath = "../Generated/frame_as_6_red.jpg"
    img =  cv2.imread(imgPath)
    img[..., :2] = 0
    cv2.imwrite(genPath, img)


partA()
partB()

