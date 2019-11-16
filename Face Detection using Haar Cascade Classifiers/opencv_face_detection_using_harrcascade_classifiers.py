import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  # declaring the classifier for faces
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')  # declaring the classifier for eyes
# image = cv2.imread('../images/face.png')

capture = cv2.VideoCapture(0)
# capture = cv2.VideoCapture('../videos/face.mp4')

while capture.isOpened():
    _, image = capture.read()

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(image_gray, 1.1, 4)  # detect the faces inside the frame

    # loop through every face detected
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 3)  # draw a rectangle around the face
        roi_gray = image_gray[y:y + h, x:x + w]  # grayscale region of interest
        roi_color = image[y:y + h, x:x + w]  # color region of interest

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 4)  # detect the eyes inside the frame

        # loop through every eyes detected
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0))  # draw a rectangle around the eyes

    cv2.imshow('Video', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cv2.waitKey(0)
# cv2.destroyAllWindows()
capture.release()
