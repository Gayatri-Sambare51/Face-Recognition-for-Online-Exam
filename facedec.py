
import os
from django.urls import path, include
import face_recognition
import cv2 

# initialize the camera
def faceCaptureSave():
        cam = cv2.VideoCapture(0)   # 0 -> index of camera
        s, frame = cam.read()
        img_counter = 0
        img=""
        if s:    # frame captured without any errors
                cv2.namedWindow("cam-test")
                cv2.imshow("cam-test",frame)
                #cv2.waitKey(0)
                cv2.destroyWindow("cam-test")
                img="/media/profil_images/{}.png".format(img_counter)
                cv2.imwrite(img, frame)
                print("{} written!".format(img))
                img_counter += 1
                print(1)

