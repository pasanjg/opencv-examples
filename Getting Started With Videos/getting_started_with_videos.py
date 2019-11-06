import cv2

capture = cv2.VideoCapture(0)  # arg-input file name or video input device index. Change index to change camera

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # add codec for the output video
output = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # output file name, video codec, framerate, frame size

print(capture.isOpened())  # returns true if video/source available

while capture.isOpened():
    ret, frame = capture.read()  # ret will be true if the video is available and frames are set

    if ret:  # if video is available, ret == TRUE

        print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))  # get other properties
        print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

        output.write(frame)  # write the video. BGR mode

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert the BGR image to grayscale
        cv2.imshow('frame', gray)  # show video. Grayscale mode

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

capture.release()
output.release()
cv2.destroyAllWindows()
