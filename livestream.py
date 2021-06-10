import cv2


capture = cv2.VideoCapture("http://192.168.1.100/video")


while(True):
	_, frame = capture.read()
	cv2imshow('livestream', frame)

	if cv2.waitKey(1) == ord('q'):
		break

capture.release()
cv2.destroyAllWindows()