import cv2


class histHelper:
    # control number of bins to create for each histogram
    def __init__(self, bins):
        self.bins = bins

    def histogram(self, imgpath):
        img = cv2.imread(imgpath)
        hist = cv2.calcHist([img], [0, 1, 2], None, self.bins, [0, 180, 0, 256, 0, 256])
        hist = cv2.normalize(hist).flatten()
        return hist

    # method to compare a histogram against all others using one of compareHists methods;
    # returns [id,score] of the top scores
    # def histCompare(self, hist):

