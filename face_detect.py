
import cv2 as cv
import winsound
img = cv.imread('Photos/group1.jpeg')
cv.imshow('Group of people', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of faces found = {len(faces_rect)}')

alarm = 0

if(len(faces_rect)<=2):
    print('crowd flow permitted')
    alarm = 0

else:
    print('crowd flow exempted')
    alarm = 1
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 10000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)
    
    



for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y),(x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)

cv.waitKey(0)

