import cv2,winsound
import os
import profiles
import numpy as np
from speaker import aprint
from profiles import videoSource
currdir = os.path.dirname(os.path.realpath(__file__)) + "\\"


def recognizeVideo(sourceType, source=currdir+'video.mp4'):
    # Create Local Binary Patterns Histograms for face recognization
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    profiles.assure_path_exists(currdir+"trainer\\")
    # Load the trained mode
    recognizer.read(currdir+'trainer\\trainer.yml')
    # Load prebuilt model for Frontal Face
    cascadePath = currdir+'haarcascade_frontalface_default.xml'
    # Create classifier from prebuilt model
    faceCascade = cv2.CascadeClassifier(cascadePath)
    font = cv2.FONT_HERSHEY_SIMPLEX

    if sourceType == videoSource.webcam:
        cam = cv2.VideoCapture(0)
    elif sourceType == videoSource.video:
        cam = cv2.VideoCapture(source)
    else:
        cam = cv2.VideoCapture(source)

    id_name = profiles.readDict()
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 6)
        for(x, y, w, h) in faces:
            cv2.rectangle(im, (x-20, y-20), (x+w+20, y+h+20), (0, 255, 0), 4)
            # Recognize the face belongs to which ID
            Id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
            Ids = " s"
            # Check the ID if exist
            if(str(Id) in id_name):
                Ids = id_name.get(str(Id)) + \
                    " {0:.5f}%".format(round(100 - confidence, 2))
                # confidence check
                if round(100 - confidence, 2) > 30:
                    cam.release()
                    cv2.destroyAllWindows()
                    return round(100 - confidence, 2), id_name.get(str(Id))
            # Put text describe who is in the picture
            cv2.rectangle(im, (x-22, y-90), (x+w+22, y-22), (0, 255, 0), -1)
            cv2.putText(im, str(Ids), (x, y-40), font, 1, (255, 255, 255), 3)
        winsound.Beep(3000,500)
        cv2.imshow('im', im)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
def recognizeImage(path):  # returns confidence%,name
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    profiles.assure_path_exists(currdir+"trainer\\")
    recognizer.read(currdir+'trainer\\trainer.yml')
    cascadePath = currdir+'haarcascade_frontalface_default.xml'
    faceCascade = cv2.CascadeClassifier(cascadePath)
    font = cv2.FONT_HERSHEY_SIMPLEX
    id_name = profiles.readDict()
    im = cv2.imread(path)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.1, 10)
    for(x, y, w, h) in faces:
        cv2.rectangle(im, (x-20, y-20), (x+w+20, y+h+20), (0, 255, 0), 4)
        Id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
        Ids = " s"
        if(str(Id) in id_name):
            #Ids = id_name.get(str(Id)) + " {0:.5f}%".format(round(100 - confidence, 2))
            Ids = " {0:.5f}%".format(round(100 - confidence, 2))
            if round(100 - confidence, 2) > 30:
                cv2.destroyAllWindows()
                return round(100 - confidence, 2), id_name.get(str(Id))
        cv2.rectangle(im, (x-22, y-90), (x+w+22, y-22), (0, 255, 0), -1)
        cv2.putText(im, str(Ids), (x, y-40), font, 1, (255, 255, 255), 3)
    cv2.imshow('im', im)
    while True:
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

# confidence,name =recognizeImage(currdir+'images\\8.png')
# print(str(confidence)+name)
aprint('Starting Identification. Please look into the camera.')
confidence, name = recognizeVideo(videoSource.video, 'http://192.168.225.99:8080/video')
aprint("Welcome to A T M system : "+name)
