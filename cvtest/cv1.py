import cv2
import numpy as np


inp_dir = 'data/'
out_dir = 'data/out/'

def diag():
    print(cv2.__file__)
    print(cv2.getBuildInformation()) # OpenCV version / build timestamp / used python paths

    # flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
    # print(flags)

    for i in dir(cv2):
        if i.startswith('COLOR_'):
            print(i)

# https://github.com/opencv/opencv/issues/8885


def convert_img(img_file):
    in_path = inp_dir + img_file
    # todo: check file exists
    out_path = out_dir + img_file
    print('convertToGrayScale', in_path, out_path)
    # img is numpy.ndarray
    img = cv2.imread(in_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print('file ' + in_path + ' not found')
        return False

    # img = cv2.imread(in_path)
    print(img.shape)

    rc = cv2.imwrite(out_path, img)
    if not rc:
        print("WRITE ERROR")
    return rc

convert_img('img1.png')
convert_img('img2.jpg')
convert_img('fract.jpeg')
convert_img('dice.jpeg')


def videoTest():
    cap = cv2.VideoCapture(0)
    while (1):
        # Take each frame
        _, im = cap.read()
        # Convert BGR to HSV
        # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # # define range of blue color in HSV
        # lower_blue = np.array([110,50,50])
        # upper_blue = np.array([130,255,255])
        # # Threshold the HSV image to get only blue colors
        # mask = cv2.inRange(hsv, lower_blue, upper_blue)
        # # Bitwise-AND mask and original image
        # res = cv2.bitwise_and(frame,frame, mask= mask)
        cv2.imshow('frame', im)
        size = cv2.GetSize(im)
        cv2.create


'''
thumbnail = cv.CreateImage( ( size[0] / 10, size[1] / 10), im.depth, im.nChannels)


    thumbnail = cv2.CreateMat(frame.rows / 10, frame.cols / 10, cv.CV_8UC3)
    cv2.Resize(frame, thumbnail)
    cv2.NamedWindow('input')
    cv2.ShowImage(frame, thumbnail)
    cv2.ShowImage(thumbnail)
    # cv2.imshow('mask',mask)
    # cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        print('Exit...')
        break
'''

cv2.destroyAllWindows()
