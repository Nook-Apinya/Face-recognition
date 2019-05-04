import cv2
import face_recognition

video_cap=cv2.VideoCapture(0)

face_location=[]

while True:
    ret,frame =video_cap.read()

    rgb_frame=frame[:,:,::-1]

    face_location=face_recognition.face_locations(rgb_frame)

    for top,right,bottom,left in face_location:
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)

    cv2.imshow('Video',frame)

    if cv2.waitKey(1)&0xff==ord('q'):
        break

video_cap.release()
cv2.destroyAllWindows()
