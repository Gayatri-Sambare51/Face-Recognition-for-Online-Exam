import cv2

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

cv2.namedWindow("test")

img_counter = 0


ret, frame = cam.read()

if not ret:
    print("failed to grab frame")
else:
    cv2.imshow("test", frame)

    img = "images/{}.png".format(img_counter)
    cv2.imwrite(img, frame)
    print("{} written!".format(img))
    img_counter += 1

    cam.release()
    img_counter += 1

    cv2.destroyAllWindows()