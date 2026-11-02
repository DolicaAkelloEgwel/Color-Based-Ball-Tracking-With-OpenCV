import cv2
import numpy as np
import yaml

WIN_NAME = "image"

points = []

vs = cv2.VideoCapture(0)


def get_point(event, x, y, flags, params):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Clicked")
        points.append((x, y))


while True:

    rval, frame = vs.read()

    if frame is None:
        break

    cv2.namedWindow(WIN_NAME)
    cv2.setMouseCallback(WIN_NAME, get_point)
    cv2.imshow(WIN_NAME, frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

    if points:

        x, y = points[-1]
        image_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        pixel = image_hsv[y, x]

        upper = [pixel[0] + 10, pixel[1] + 10, pixel[2] + 40]
        lower = [pixel[0] - 10, pixel[1] - 10, pixel[2] - 40]

        image_mask = cv2.inRange(image_hsv, np.array(lower), np.array(upper))
        cv2.imshow("mask", image_mask)

        hsv_range = {
            "upper": [int(val) for val in upper],
            "lower": [int(val) for val in lower],
        }

        with open("config.yaml", "w") as f:
            yaml.dump(hsv_range, f, default_flow_style=False)

        points.clear()

cv2.destroyAllWindows()
