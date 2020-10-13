import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2

# open webcam
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()
    

# loop through frames
while webcam.isOpened():

    # read frame from webcam 
    status, frame = webcam.read()

    if not status:
        print("Could not read frame")
        exit()

    # apply object detection
    # bbox, label, conf = cv.detect_common_objects(frame,confidence=0.01,model='yolov3-tiny')
    bbox, label, conf = cv.detect_common_objects(frame)

    # indices = []

    # for i, l in enumerate(label):
    #     if l != "spoon":
    #         indices.append(i)
    # for i in sorted(indices, reverse=True):
    #     del label[i]
    #     del bbox[i]
    #     del conf[i]

    # draw bounding box over detected objects
    out = draw_bbox(frame, bbox, label, conf)

    # display output
    cv2.imshow("Real-time object detection", out)

    # press "Q" to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# release resources
webcam.release()
cv2.destroyAllWindows()        