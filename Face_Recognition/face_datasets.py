import cv2
import profiles
import os
currdir = os.path.dirname(os.path.realpath(__file__)) + "\\"

#vid_cam = cv2.VideoCapture(0)
vid_cam = cv2.VideoCapture(currdir+'video001.mp4')

face_detector = cv2.CascadeClassifier(
    currdir+'haarcascade_frontalface_default.xml')
face_id = int(input("Enter Id:"))
if not profiles.userExist(face_id):
    name = str(input('Enter your name:'))
    profiles.addUser(face_id, name)
else:
    print('welcome back ' + profiles.getUser(face_id))
profiles.assure_path_exists(currdir+"dataset\\" + str(face_id) + "\\")
count = len(os.listdir(currdir+"dataset\\" + str(face_id)))
initcount = count
while(True):
    _, image_frame = vid_cam.read()    # Capture video frame
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:    # Loops for each faces
        cv2.rectangle(image_frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        count += 1
        cv2.imwrite(currdir+"dataset\\"+str(face_id)+"\\User." + str(face_id) + '.' +
                    str(count) + ".jpg", gray[y:y+h, x:x+w])        # Save the captured image into the datasets folder
        cv2.imshow('frame', image_frame)  # display the video frame
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    elif count > initcount + 100:    # If image taken reach 100, stop taking video
        break
vid_cam.release()  # Stop video
cv2.destroyAllWindows()  # Close all started windows
