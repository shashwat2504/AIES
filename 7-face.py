# %pip install opencv-python matplotlib

import cv2
import matplotlib.pyplot as plt
%matplotlib inline


# Get image and cascade names
imagePath = "image.jpg"
cascPath = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


RGB_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(RGB_img)
plt.show()

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
)

print("Found {} faces!".format(len(faces)))


# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h),
                  (0, 255, 0), 2)

RGB_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(RGB_img)
plt.show()













# import cv2
# import matplotlib.pyplot as plt

# image = cv2.imread("2.png")
# faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# if image is None:
#     print("Error: Image not found!")
#     exit()

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.show()

# faces = faceCascade.detectMultiScale(gray)

# print("Found {} faces!".format(len(faces)))

# for (x, y, w, h) in faces:
#     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.show()
