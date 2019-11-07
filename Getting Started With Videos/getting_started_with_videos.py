import cv2
import datetime

capture = cv2.VideoCapture(0)  # arg-input file name or video input device index. Change index to change camera

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # add codec for the output video
output = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # output file name, video codec, framerate, frame size

print(capture.isOpened())  # returns true if video/source available

while capture.isOpened():
    ret, frame = capture.read()  # ret will be true if the video is available and frames are set

    if ret:  # if video is available, ret == TRUE

        # setting frame size
        capture.set(3, 640)  # 3 - PROP index for WIDTH
        capture.set(4, 480)  # 4 - PROP index for HEIGHT

        # WIDTH and HEIGHT will take only the values which are available for the camera

        print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))  # get other properties
        print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(capture.get(3)) + ' Height: ' + str(capture.get(4))
        dateTime = str(datetime.datetime.now())
        frame = cv2.putText(frame, str(text + ' ' + dateTime), (10, 50), font, 0.5, (0, 255, 255), 1, cv2.LINE_AA)

        # output.write(frame)  # write the video. BGR mode

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert the BGR image to grayscale
        cv2.imshow('frame', frame)  # show video. Grayscale mode

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

capture.release()
output.release()
cv2.destroyAllWindows()
