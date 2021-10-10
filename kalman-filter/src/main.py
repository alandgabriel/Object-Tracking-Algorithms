import cv2

import numpy as np

def getBallXY (frame):
    lowerB = np.array([130, 30, 0], dtype = 'uint8')
    upperB = np.array([255, 255, 90], dtype = 'uint8')
        #extract mask of green objects
    greenM = cv2.inRange(frame, lowerB, upperB)
        #morphological filter to dilate mask
    kernel = np.ones((5, 5), np.uint8)
    greenMaskDilated = cv2.dilate(greenM, kernel)

        # Find ball blob as it is the biggest green object in the frame
    [nLabels, labels, stats, centroids] = cv2.connectedComponentsWithStats(greenMaskDilated, 8, cv2.CV_32S)

        # First biggest contour is image border always, Remove it
    stats = np.delete(stats, (0), axis = 0)
        
    maxBlobIdx_i, maxBlobIdx_j = np.unravel_index(stats.argmax(), stats.shape)

        # This is our ball coords that needs to be tracked
    ballX = stats[maxBlobIdx_i, 0] + (stats[maxBlobIdx_i, 2]/2)
    ballY = stats[maxBlobIdx_i, 1] + (stats[maxBlobIdx_i, 3]/2)
    return ballX, ballY

class KF:
    def __init__(self):
        self.kf = cv2.KalmanFilter (4,2)
        self.kf.measurementMatrix = np.array([[1,0,0,0], [0,1,0,0]], np.float32)
        self.kf.transitionMatrix = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32)
    def correct(self,xpos,ypos):
        measured = np.array([[np.float32(xpos)], [np.float32(ypos)]])
        self.kf.correct(measured)
    def predict (self):
        predicted = self.kf.predict()
        return predicted


kf = KF()
vid = cv2.VideoCapture('ball.mp4')
i = 0
while (vid.isOpened()):
    rc, frame = vid.read()
    if (rc == True):
        if(True): #(i<40):
            xp, yp = getBallXY (frame)
            # Draw Actual coords from segmentation
            cv2.circle(frame, (int(xp), int(yp)), 20, [255,0,0], 2, 8)
            # correcting model with measurements
            kf.correct(xp,yp)
        #predict ball position with KF model
        predXY = kf.predict()    
         # Draw Kalman Filter Predicted output
        cv2.circle(frame, (predXY[0], predXY[1]), 20, [0,255,255], 2, 8)
        cv2.imshow('Input', frame)
        i += 1
        if (cv2.waitKey(100) & 0xFF == ord('q')):
            break

    else:
        break

vid.release()
cv2.destroyAllWindows()

