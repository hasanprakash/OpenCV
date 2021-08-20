import urllib.request
import cv2
import numpy as np
import ssl

# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

url = 'http://192.168.1.16:8080/shot.jpg'

img_counter = 0

while True:

    imgResp = urllib.request.urlopen(url)

    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)
    cv2.imshow('temp',cv2.resize(img,(600,400)))
    q = cv2.waitKey(1)
    if q == ord("q") or q == ord('x') or q%256 == 27:
        break
    elif q%256 == 32:
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, img)
        print("{} file saved!!".format(img_name))
        img_counter += 1

cv2.destroyAllWindows()




# import urllib.request
# import numpy as np
# import cv2

# url = 'http://192.168.1.16:8080/shot.jpg'

# while True:

#     urlResponse = urllib.request.urlopen(url)
#     imgnp = np.array(bytearray(urlResponse.read()), dtype=np.uint8)
#     img = cv2.imdecode(imgnp, -1)
#     cv2.imshow('test', img)
#     q = cv2.waitKey(10)
#     print(q)
#     if q == ord('q') or q==ord('x'):
#         exit(0)
























# import cv2

# cam = cv2.VideoCapture(0)

# cv2.namedWindow("test")

# img_counter = 0

# while True:
#     ret, frame = cam.read()
#     if not ret:
#         print("failed to grab frame")
#         break
#     cv2.imshow("test", frame)

#     k = cv2.waitKey(1)
#     if k%256 == 27:
#         # ESC pressed
#         print("Escape hit, closing...")
#         break
#     elif k%256 == 32:
#         # SPACE pressed
#         img_name = "opencv_frame_{}.png".format(img_counter)
#         cv2.imwrite(img_name, frame)
#         print("{} written!".format(img_name))
#         img_counter += 1

# cam.release()

# cv2.destroyAllWindows()




