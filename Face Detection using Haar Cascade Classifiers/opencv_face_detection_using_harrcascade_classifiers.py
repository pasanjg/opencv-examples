import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  # declaring the classifier
# image = cv2.imread('../images/face.png')

capture = cv2.VideoCapture(0)
# capture = cv2.VideoCapture('../videos/face.mp4')

while capture.isOpened():
    _, image = capture.read()

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(image_gray, 1.1, 4)  # detect the faces inside the frame

    # loop through every face
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 3)

    cv2.imshow('Video', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cv2.waitKey(0)
# cv2.destroyAllWindows()
capture.release()
