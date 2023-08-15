import cv2 as cv
import winsound
capture = cv.VideoCapture('Videos/group.mp4')

while True:
    isTrue, frame = capture.read()
    haar_cascade = cv.CascadeClassifier('haar_face.xml')

    faces_rect = haar_cascade.detectMultiScale(
        frame, scaleFactor=1.3,
        minNeighbors=4,
        minSize=(30, 30),
        flags=cv.CASCADE_SCALE_IMAGE)

    print(f'Number of faces found = {len(faces_rect)}')

    alarm = 0

    if (len(faces_rect) <= 2):
        print('crowd flow permitted')
        alarm = 0

    else:
        print('crowd flow exempted')
        alarm = 1

    if (alarm == 1):
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 5000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)

    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

    cv.imshow('Detected Faces', frame)
    # cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
