from SandD import SnD
import cv2
import matplotlib.pyplot as plt
import numpy as np
from circles import InternProj
from click import SetSandD as clickobj

img = cv2.imread('opencv_frame_0.png')
# img = cv2.imread('indiamap5.jpg')
h, w, c = img.shape
img = cv2.resize(img, (w//2, h//2))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
xcnts = []


binary_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 131, 15)
# plt.imshow(binary_img)
# plt.show()
nop, nop, boxes, nop = cv2.connectedComponentsWithStats(binary_img)
boxes = boxes[1:]
filtered_boxes = []
for x,y,w,h,pixels in boxes:
    if pixels < 10000 and h < 300 and w < 300 and h > 5 and w > 5:
        filtered_boxes.append((x,y,w,h))
for x,y,w,h in filtered_boxes:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255),2)
    xcnts.append([x, y])

plt.imshow(img)
plt.show()


img_copy = img.copy()
        
  
# print("first dot", xcnts[0])
print("\n{} dots found!!".format(len(xcnts)))

img_copy = cv2.cvtColor(img_copy, cv2.COLOR_GRAY2RGB)


obj = InternProj()
obj.hasan = xcnts
[img_after_circles, alldots] = obj.addcircle(img_copy)


# OPTIONAL
plt.imshow(img_after_circles)
plt.show()

SnD.img = img_after_circles

# CALLING CLICK FUNCTION

# clickobj = SetSandD()
clickobj.alldots = alldots
cv2.namedWindow('image')

while (True):
    cv2.setMouseCallback('image', clickobj(img_after_circles).mouseleftclick)

    # img_after_circles = cv2.resize(img_after_circles, (600, 400))
    cv2.imshow('image', img_after_circles)


    
    if cv2.waitKey(10) == ord('q'):
        break



























# # x = np.where(np.all(img <= 80, axis=-1))
# x = np.where(np.any(img <= 80, axis=-1))

# for i in x:
#     print(i)
# img_copy = img.copy()
# img_copy[x] = [255]
# img_copy = cv2.cvtColor(img_copy, cv2.COLOR_GRAY2RGB)

# plt.imshow(img_copy)
# plt.show()












# # threshold
# th, threshed = cv2.threshold(img, 1, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
  
# # findcontours
# cnts = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]
  
# # area range
# # a1 = 400
# # a2 = 1000
# a1 = 150
# # a2 = 250
# a2 = 500


  
# # for cnt in cnts:
    
# #     if a1<cv2.contourArea(cnt) <a2:
# #         xcnts.append(cnt)
# #         print(cnt)
#         # print(cv2.contourArea(cnt))