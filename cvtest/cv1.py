import cv2
import numpy as np

img_dir = 'data/'
inp = dir + 'img1.png'


def convertToGrayScale(in_path=img_dir+inp, out_path=img_dir+'out/'+inp):
    image = cv2.imread(in_path, 0)
    cv2.imwrite(out_path, image)



#flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
#print(flags)

#grayImage = cv2.imread(input, cv2.COLOR_BGR2GRAY)
#cv2.imwrite(dir + 'bw.png', grayImage)

cap = cv2.VideoCapture(0)
while(1):
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
    print(size)
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
