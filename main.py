import cv2
#import numpy as np
import time
import winsound as sound
import pyttsx3

face_cascade = cv2.CascadeClassifier('./Haar/haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier('./Haar/haarcascade_eye_tree_eyeglasses.xml')

cap = cv2.VideoCapture(0)

i = 0
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
##      cv2.rectangle(image, start_point, end_point, color, thickness)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray,1.3,5)
        for (ex,ey,ew,eh) in eyes:
##            cv2.rectangle(roi_color,(ex+ew,ey+eh),(ex,ey),(0,255,0),1)

            cv2.circle(roi_color,(ex+int(ew/2),ey+int(eh/2)),(int(ew/2)),(0,255,0),1)
##          cv2.circle(image, center_coordinates, radius, color, thickness)
##            cv2.ellipse(roi_color,((ex-10)+int(ew/2),(ey-10)+int(eh/2)),(int(ew/2),int(eh/2)),0,0,360,(0,255,0),1)
##            print("x:",int(ex/2),"y:",int(ey/2),"ew:",int(ew/2),"eh:",int(eh/2))
        if len(eyes) == 0:
            i+=1
            if i>5:
                voice = pyttsx3.init()
                voice.say("Hey Please Wake Up... stay awake...")
                voice.runAndWait()
                sound.PlaySound('./alarm.wav',sound.SND_ALIAS)
                print("Please Wake Up...")
        else:
            i = 0

    cv2.imshow("eyes",img)

    if cv2.waitKey(30) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

