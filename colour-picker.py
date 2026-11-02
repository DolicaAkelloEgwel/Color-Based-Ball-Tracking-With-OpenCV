import cv2

WIN_NAME = "image"

no_colour_selected = True

vs = cv2.VideoCapture(0)


def pick_colour(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Clicked", x, y)


while no_colour_selected:

    rval, frame = vs.read()

    if frame is None:
        break

    cv2.namedWindow(WIN_NAME)
    cv2.setMouseCallback(WIN_NAME, pick_colour)
    cv2.imshow(WIN_NAME, frame)

    key = cv2.waitKey(1) & 0xFF

    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break

cv2.destroyAllWindows()
