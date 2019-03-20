import numpy as np
import cv2
import sys

imagePath = 'E:\\projects\\python-ai-scripts\\CSK_HELMET\\face.jpg'
helmetImagePath = 'E:\\projects\\python-ai-scripts\\CSK_HELMET\\helmet.png'
cascPath = 'E:\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml'
# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)
#################
# Load our overlay image: mustache.png
#imgMustache = cv2.imread('mustache.png',-1)
imgMustache = cv2.imread(helmetImagePath)
 
# Create the mask for the mustache
orig_mask = imgMustache[:,:,2]
 
# Create the inverted mask for the mustache
orig_mask_inv = cv2.bitwise_not(orig_mask)
 
# Convert mustache image to BGR
# and save the original image size (used later when re-sizing the image)
imgMustache = imgMustache[:,:,0:3]
origMustacheHeight, origMustacheWidth = imgMustache.shape[:2]
 

#################
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


# Draw a rectangle around the faces
for (nx, ny, nw, nh) in faces:
    # The mustache should be three times the width of the nose
    roi_gray = gray[ny:ny+nh, nx:nx+nw]
    roi_color = image[ny:ny+nh, nx:nx+nw]
 
    mustacheWidth =   int(5 * nw+50)
    mustacheHeight = mustacheWidth * origMustacheHeight / origMustacheWidth

    # Center the mustache on the bottom of the nose
    x1 = nx - (mustacheWidth/4)
    x2 = nx + nw + (mustacheWidth/4)
    y1 = ny + nh - (mustacheHeight/2)
    y2 = ny + nh + (mustacheHeight/2)

    # Check for clipping
    if x1 < 0:
        x1 = 0
    if y1 < 0:
        y1 = 0
    if x2 > nw:
        x2 = nw
    if y2 > nh:
        y2 = nh

    # Re-calculate the width and height of the mustache image
    mustacheWidth = x2 - x1
    mustacheHeight = y2 - y1

    # Re-size the original image and the masks to the mustache sizes
    # calcualted above
    mustache = cv2.resize(imgMustache, (mustacheWidth,mustacheHeight), interpolation = cv2.INTER_AREA)
    mask = cv2.resize(orig_mask, (mustacheWidth,mustacheHeight), interpolation = cv2.INTER_AREA)
    mask_inv = cv2.resize(orig_mask_inv, (mustacheWidth,mustacheHeight), interpolation = cv2.INTER_AREA)

    # take ROI for mustache from background equal to size of mustache image
    roi = roi_color[y1:y2, x1:x2]

    # roi_bg contains the original image only where the mustache is not
    # in the region that is the size of the mustache.
    roi_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

    # roi_fg contains the image of the mustache only where the mustache is
    roi_fg = cv2.bitwise_and(mustache,mustache,mask = mask)

    # join the roi_bg and roi_fg
    dst = cv2.add(roi_bg,roi_fg)

    # place the joined image, saved to dst back over the original image
    roi_color[y1:y2, x1:x2] = dst

    break
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
