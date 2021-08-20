import cv2
from SandD import SnD
from graph import Graph
from start import Start
from reset import Reset

class SetSandD:
    Hello = False
    obj = SnD()
    graphobj = Graph()
    startobj = Start()
    alldots = []
    radius = 20
    color = (0, 255, 0)
    thickness = 3
    count = 0
    w, h = 0, 0
    def __init__(self, img_after_circles):
        self.img_after_circles = img_after_circles
        self.w, self.h, c = img_after_circles.shape
    def mouseleftclick(self, event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            SetSandD.Hello = True
            if SetSandD.count == 2:
                if x>50 and x <=141 and y>=30 and y<=51:
                    self.startobj.start()
                elif x>=813 and y>=29 and x <=905 and y<=51:
                    SetSandD.Hello = False
                    SetSandD.count = 0
                    self.img_after_circles = cv2.circle(self.img_after_circles, SnD.source, self.radius, (255, 0, 0), self.thickness)
                    self.img_after_circles = cv2.circle(self.img_after_circles, SnD.destination, self.radius, (255, 0, 0), self.thickness)
                    SnD.source = None
                    SnD.destination = None
                    SnD.alldots = []
                    Graph.g = []
            for i in range(len(self.alldots)):
                dis = self.radius*self.radius - (pow(x-self.alldots[i][0], 2) + pow(y-self.alldots[i][1], 2))
                if dis > 0:
                    # print(self.count)
                    if SetSandD.count<2:
                        self.img_after_circles = cv2.circle(self.img_after_circles, self.alldots[i], self.radius, self.color, self.thickness)
                        SetSandD.count += 1
                    else:
                        SetSandD.count += 1
                        
                    if SetSandD.count == 1:
                        SnD.source = self.alldots[i]
                        print("SOURCE = ", self.obj.source)
                        print("DESTINATION = ", self.obj.destination)
                    elif SetSandD.count == 2:
                        if self.alldots[i] == self.obj.source:
                            SetSandD.count -= 1
                        else:
                            SnD.destination = self.alldots[i]
                            print("SOURCE = ", self.obj.source)
                            print("DESTINATION = ", self.obj.destination)
                            SnD.alldots = self.alldots
                            # self.graphobj.alldots = self.alldots
                            self.graphobj.createGraph(self.alldots)
                            self.img_after_circles = cv2.putText(self.img_after_circles, 'START', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                            self.img_after_circles = cv2.putText(self.img_after_circles, 'RESET', (self.h-150, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                            cv2.namedWindow("image")
                            

            cv2.imshow('image', self.img_after_circles)



