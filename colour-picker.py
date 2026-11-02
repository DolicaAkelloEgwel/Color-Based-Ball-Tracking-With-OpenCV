import cv2
import numpy as np

WIN_NAME = "image"

points = []

vs = cv2.VideoCapture(0)


def pick_colour(event, x, y, flags, params):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Clicked")
        points.append((x, y))


while True:

    rval, frame = vs.read()

    if frame is None:
        break

    cv2.namedWindow(WIN_NAME)
    cv2.setMouseCallback(WIN_NAME, pick_colour)
    cv2.imshow(WIN_NAME, frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

    if points:

        x, y = points[-1]
        image_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        pixel = image_hsv[y, x]

        upper = np.array([pixel[0] + 10, pixel[1] + 10, pixel[2] + 40])
        lower = np.array([pixel[0] - 10, pixel[1] - 10, pixel[2] - 40])

        image_mask = cv2.inRange(image_hsv, lower, upper)
        cv2.imshow("mask", image_mask)

        points.clear()

cv2.destroyAllWindows()
