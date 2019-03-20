import numpy as np
import cv2
import sys

imagePath = 'E:\\projects\\python-ai-scripts\\CSK_HELMET\\face2.jpg'
helmetImagePath = 'E:\\projects\\python-ai-scripts\\CSK_HELMET\\helmet.png'
cascPath = 'E:\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml'
# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)
#################
# Load our overlay image: mustache.png
#imgMustache = cv2.imread('mustache.png',-1)
imgMustache = cv2.imread(helmetImagePath)
# Read the image
image = cv2.imread(imagePath)
image = np.array(image, dtype=np.uint8)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
    ,flags = cv2.CASCADE_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))
 
def transparentOverlay(src, overlay, pos=(0, 0), scale=1):
    overlay = cv2.resize(overlay, (0, 0), fx=scale, fy=scale)
    h, w, _ = overlay.shape  # Size of foreground
    rows, cols, _ = src.shape  # Size of background Image
    y, x = pos[0], pos[1]  # Position of foreground/overlay image
 
    # loop over all pixels and apply the blending equation
    for i in range(h):
        for j in range(w):
            if x + i >= rows or y + j >= cols:
                continue
            alpha = float(overlay[i][j][2] / 255.0)  # read the alpha channel
            src[x + i][y + j] = alpha * overlay[i][j][:3] + (1 - alpha) * src[x + i][y + j]
    return src
 
# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    glass_symin = int(y + -3.8 * h / 6)
    glass_symax = int(y + 7.5 * h / 6)
    sh_glass = glass_symax - glass_symin
    sh_glass +=5
    face_glass_roi_color = image[glass_symin:glass_symax, x-5:(x+w)*4]
    
    specs = cv2.resize(imgMustache, (w, sh_glass),interpolation=cv2.INTER_CUBIC)
    transparentOverlay(face_glass_roi_color,specs)
    #cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
