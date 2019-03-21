import cv2,os ,profiles
import numpy as np

currdir = os.path.dirname(os.path.realpath(__file__)) + "\\"

id_name=profiles.readDict()

# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.LBPHFaceRecognizer_create()

profiles.assure_path_exists(currdir+"trainer\\")

# Load the trained mode
recognizer.read(currdir+'trainer\\trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = currdir+'haarcascade_frontalface_default.xml'

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath)

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize and start the video frame capture
cam = cv2.VideoCapture(currdir+'video001.mp4')


# Loop
while True:
    # Read the video frame
    ret, im =cam.read()

    # Convert the captured frame into grayscale
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    # Get all face from the video frame
    faces = faceCascade.detectMultiScale(gray, 1.2 , 6)

    # For each face in faces
    for(x,y,w,h) in faces:

        # Create rectangle around the face
        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

        # Recognize the face belongs to which ID
        Id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        Ids=" s"
        # Check the ID if exist 
        if(str(Id) in id_name):
            Ids = id_name.get(str(Id)) + " {0:.5f}%".format(round(100 - confidence, 2))
        #confidence check
            if round(100 - confidence, 2) > 80:
                print(id_name.get(str(Id)) + " detected")
                exit(5)

        # Put text describe who is in the picture
        cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
        cv2.putText(im, str(Ids), (x,y-40), font, 1, (255,255,255), 3)

    # Display the video frame with the bounded rectangle
    cv2.imshow('im',im) 

    # If 'q' is pressed, close program
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Stop the camera
cam.release()

# Close all windows
cv2.destroyAllWindows()
