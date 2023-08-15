import cv2
import winsound
window_name = "Detected Objects in webcam"
video = cv2.VideoCapture(0)

while video.isOpened():
    ret, frame = video.read()

    haar_cascade = cv2.CascadeClassifier('haar_face.xml')

    faces_rect = haar_cascade.detectMultiScale(frame, scaleFactor=1.3,
                                               minNeighbors=4,
                                               minSize=(30, 30),
                                               flags=cv2.CASCADE_SCALE_IMAGE)

    print(f'Number of faces found = {len(faces_rect)}')

    alarm = 0

    if (len(faces_rect) >= 2):
        print('crowd flow permitted')
        alarm = 0

    else:
        print('crowd flow exempted')
        alarm = 1

    if (alarm == 1):
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 1000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)

    for (x, y, w, h) in faces_rect:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

    if not ret:
        break
    cv2.imshow(window_name, frame)
    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()
