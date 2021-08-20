# I am creating a circle around point!
import cv2

class InternProj:
    hasan = []
    def addcircle(self, img):
        alldots = []
        for i in range(len(self.hasan)):
            # center = (self.hasan[i][0][0][0]+5, self.hasan[i][0][0][1]+10)
            # alldots.append([self.hasan[i][0][0][0]+5, self.hasan[i][0][0][1]+10])
            center = (self.hasan[i][0]+5, self.hasan[i][1]+10)
            alldots.append([self.hasan[i][0]+5, self.hasan[i][1]+10])
            radius = 20
            color = (255, 0, 0)
            thickness = 3
            img = cv2.circle(img, center, radius, color, thickness)
        
        return [img, alldots]

    
