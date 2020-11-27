import cv2

cap = cv2.VideoCapture(0)

result = True
while(result):
    ret,frame = cap.read()
    cv2.imwrite("NewPicture.jpg",frame)
    result = False
    
cap.release()
cv2.destroyAllWindows()
