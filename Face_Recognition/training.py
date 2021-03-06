import cv2
import os
import numpy as np
from PIL import Image
currdir = os.path.dirname(os.path.realpath(__file__)) + "\\"

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
def getImagesAndLabels(path):
    # Get all file path
    # Initialize empty face sample
    faceSamples = []

    # Initialize empty id
    ids = []
    idsx = os.listdir(path)
    imagePaths = []
    for id in idsx:
        for f in os.listdir(path+""+str(id)+"\\"):
            imagePaths.append(path+""+str(id)+"\\"+f)

    # Loop all the file path
    for imagePath in imagePaths:

        # Get the image and convert it to grayscale
        PIL_img = Image.open(imagePath).convert('L')

        # PIL image to numpy array
        img_numpy = np.array(PIL_img, 'uint8')

        # Get the image id
        id = int(os.path.split(imagePath)[-1].split(".")[1])

        # Get the face from the training images
        faces = detector.detectMultiScale(img_numpy)

        # Loop for each face, append to their respective ID
        for (x, y, w, h) in faces:

            # Add the image to face samples
            faceSamples.append(img_numpy[y:y+h, x:x+w])

            # Add the ID to IDs
            ids.append(id)

    # Pass the face array and IDs array
    return faceSamples, ids
def generateTrainingModel(path=currdir+'trainer\\'):
    # Create Local Binary Patterns Histograms for face recognization
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # Get the faces and IDs
    faces, ids = getImagesAndLabels(currdir+'dataset\\')
    # Train the model using the faces and IDs
    recognizer.train(faces, np.array(ids))
    # Save the model into trainer.yml
    assure_path_exists(path)
    recognizer.save(path+'trainer.yml')

detector = cv2.CascadeClassifier(currdir+'haarcascade_frontalface_default.xml')
generateTrainingModel()
