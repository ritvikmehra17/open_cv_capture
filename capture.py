import cv2
cap=cv2.VideoCapture(0)
while True:
    # Capture frame-by-frame
    ret, frame=cap.read()

    # Our operations on the frame come here
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # Display the resulting framecv2.imshow('gray',gray)
    cv2.imshow('colored',frame)
    cv2.imshow('gray',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# when everything done, release the Capture
cap.release()
cv2.destroyedAllWindows()       