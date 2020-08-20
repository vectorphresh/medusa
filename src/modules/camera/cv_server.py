import base64
import cv2
import zmq

context = zmq.Context()
footage_socket = context.socket(zmq.PUB)
footage_socket.connect('tcp://localhost:5555')

camera = cv2.VideoCapture(0)  # init the camera
# cameria = picamera.PiCamera(resolution='1200x1600', framerate=24) as camera:
# output = StreamingOutput() 
# camera.rotation = 90
#
#
#

while True:
    try:
        grabbed, frame = camera.read()  # grab the current frame
        frame = cv2.resize(frame, (1200, 1600))  # resize the frame
        encoded, buffer = cv2.imencode('.jpg', frame)
        jpg_as_text = base64.b64encode(buffer)
        footage_socket.send(jpg_as_text)

    except KeyboardInterrupt:
        camera.release()
        cv2.destroyAllWindows()
        break