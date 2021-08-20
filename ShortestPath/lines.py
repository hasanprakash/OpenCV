import cv2
from SandD import SnD

class PlotLine:
    def plotLine():
        dots = SnD.alldots
        # hasan = [SnD.s] + SnD.sPath + [SnD.d]
        hasan = SnD.sPath
        for i in range(1, len(hasan)):
            first_point = (dots[hasan[i-1]][0], dots[hasan[i-1]][1])
            last_point = (dots[hasan[i]][0], dots[hasan[i]][1])
            color = (0, 255, 0)
            thickness = 2
            SnD.img = cv2.line(SnD.img, first_point, last_point, color, thickness)
            cv2.imshow('image', SnD.img)
            # cv2.putText(SnD.img, 'Min No.of lines-'+str(len(SnD.alldots)-1), (200, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

