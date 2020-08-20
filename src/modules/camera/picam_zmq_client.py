import base64
import cv2
import zmq
import time
import io
import picamera
import picamera.array
import numpy as np

context = zmq.Context()
footage_socket = context.socket(zmq.PUB)
footage_socket.connect('tcp://192.168.1.11:5555')

camera = picamera.PiCamera()
camera.start_preview()
time.sleep(2)
camera.resolution = (1200,1600)
camera.framerate = 60
camera.rotation = 90
camera.iso = 1600
rawCapture =  picamera.array.PiRGBArray(camera, size=(1200, 1600))

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array
	# show  the frame
	try:
		encoded, buffer = cv2.imencode('.png', image)
		img_as_text = base64.b64encode(buffer)
		footage_socket.send(img_as_text)
		key = cv2.waitKey(1) & 0xFF
		# clear the stream in preparation for the next frame
		rawCapture.truncate(0)
		# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			break		
	except KeyboardInterrupt:
		camera.close()
		cv2.destroyAllWindows()
		break


