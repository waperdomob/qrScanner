import cv2

import numpy as np

def qrLector():
    capture = cv2.VideoCapture(1000) #this is for deploy if not works try with 44
    #capture = cv2.VideoCapture(0) #this is for local envioronment
    data = None
    while(capture.isOpened()):
        ret, frame = capture.read()
        if (cv2.waitKey(1) == ord('s')):
            break
        qrDetector = cv2.QRCodeDetector()
        data, bbox, rectifiedImage = qrDetector.detectAndDecode(frame)
        if len(data)>0:
            cv2.imshow('webCam', rectifiedImage)
        else:
            cv2.imshow('webCam', frame)
        if (data):
            capture.release()
            break
    cv2.destroyAllWindows()
    return data


    """
        while(self.video.isOpened()):
            ret, frame = self.video.read()
            if (cv2.waitKey(1) == ord('s')):
                break
            qrDetector = cv2.QRCodeDetector()
            data, bbox, rectifiedImage = qrDetector.detectAndDecode(frame)
            if len(data)>0:
                cv2.imshow('webCam', rectifiedImage)
            else:
                cv2.imshow('webCam', frame)
            if (data):
                self.video.release()
                break
        cv2.destroyAllWindows()
        return data
    """