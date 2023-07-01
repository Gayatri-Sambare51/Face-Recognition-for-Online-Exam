from django.db import models
import os
from django.urls import path, include
import face_recognition
import cv2 

# Create your models here.


def faceCaptureSave(username):
         
        cam = cv2.VideoCapture(0,cv2.CAP_ANY)   # 0 -> index of camera
        s, frame = cam.read()
        img_counter = 0
        print(s, type(frame))
        img=""
        
        if s:    # frame captured without any errors
                # cv2.namedWindow("cam-test")
                # cv2.imshow("cam-test",frame)
                # #cv2.waitKey(0)
                # cv2.destroyWindow("cam-test")
                img="media/{}.jpg".format(username)
                cv2.imwrite(img, frame)
                
                print("{} written!".format(img))
                img_counter += 1
                
                img = str(img)
                return img
        
        else:
                #cv2.waitKey(0)
                # cv2.destroyWindow("cam-test")
                print("Read not worked") 
                

face_1_face_encoding=""
def facerecognize(user):
        check = False          
        try:
                
                cam = cv2.VideoCapture(0,cv2.CAP_V4L2)   # 0 -> index of camera
                s, img = cam.read()
               
                if s:    
                        # frame captured without any errors
                      
                        # cv2.namedWindow("cam-test")
                        # print("e4")
                        # cv2.imshow("cam-test",img)
                        # #cv2.waitKey(0)s
                        # cv2.destroyWindow("cam-test")
                        
                        
                        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                        MEDIA_ROOT =os.path.join(BASE_DIR,'faceapp')
                        
                        userimg = user+".jpg"
                        loc="media/"+userimg
                        
                        # Image from database
                        face_1_image = face_recognition.load_image_file(loc)
                        face_1_face_encoding = face_recognition.face_encodings(face_1_image)[0]
                       
                        
                        # Current Image 
                        # current_image = face_recognition.load_image_file(img)
                        face_encodings = face_recognition.face_encodings(img)[0]
                     
                        
                        try: 
                                check=face_recognition.compare_faces([face_encodings], face_1_face_encoding)
                                if check[0]:
                                        return True
                               
                        except: 
                                print("Exception")
                                if(face_encodings is not None):
                                        return True
                else:
                        print("Read not worked") 
                                        

        except :
                check = False
                print("except")
        return False
