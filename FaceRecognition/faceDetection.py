import cv2
from lineNotifyMessage import lineNotifyMessage
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0) #get the camera
cap.set(3,960) # set Width
cap.set(4,720) # set Height
count = 0 #count
while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    # when face is detected 
    for (x,y,w,h) in faces:
        count+=1
        if count < 5:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
        
        if count >= 5:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            if count == 5:
                # Save the captured image into the datasets folder
                cv2.imwrite("face.jpg", img[y:y+h, x:x+w])
                cv2.imwrite("body.jpg", img[0:479,0:639])
                
                # send a notify to LINE
                token = 'w5uwWcnzXeopwb0OLoDuwnX4XB2g1v0cQ3xWvCDSsC1'
                picURI1 = 'face.jpg'
                picURI2 = 'body.jpg'

                lineNotifyMessage(token,picURI1,picURI2)
                count+=1
    # show the window
    cv2.imshow('video',img)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()