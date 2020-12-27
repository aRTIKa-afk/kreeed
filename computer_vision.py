import cv2
import os
i=0
print ( str(i) )
i+=1
print ( str(i) )
i+=1
print ( str(i) )
capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
name='normal'
while True:
	rec, img = capture.read()

	faces = face_cascade.detectMultiScale(img, scaleFactor=2.0, minNeighbors=5, minSize=(20, 20))
	for (x, y, w, h) in faces:
		if name!='normal':
			face=cv2.imread(name+'.png')
			Wf=face.shape[1]
			Hf=face.shape[0]
			img[y:y+h, x:x+w] = cv2.resize(face, None, fx=w/Wf, fy=h/Hf, interpolation = cv2.INTER_CUBIC)[0:w, 0:h]
	cv2.imshow('hello',img)
	k = cv2.waitKey(10) & 0xFF
	if k == 27:
		break
	elif k == 32:
		name = input()

capture.release()
cv2.destroyAllWindows()
