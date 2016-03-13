from __future__ import print_function
import sys
import cv2
import csv
import numpy
from .models import IMGFile
import os
from django.conf import settings


def create_histogram(pk):
    img_file = IMGFile.objects.get(pk=pk)
    img = cv2.imread(img_file.imgFile.url[1::])
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0, 1, 2], None, [10, 10, 10], [0, 180, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    row_count = sum(1 for row in csv.reader(open(os.path.join(settings.MEDIA_ROOT, 'histograms.csv'))))
    img_file.csv_index = row_count
    img_file.save()
    print('in create_histogram with row count/cvs_index of: ', img_file.csv_index, end='\n', file=sys.stdout.flush())
    with open(os.path.join(settings.MEDIA_ROOT, 'histograms.csv'), 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(hist)
    return compare(img_file.csv_index)


def compare(index):
    if index == 0:
        return []
    else:
        d_list = {}
        hist_data = numpy.loadtxt(os.path.join(settings.MEDIA_ROOT, 'histograms.csv'), delimiter=',', dtype='float32')
        for i in range(index):
            d_list[i] = cv2.compareHist(hist_data[index], hist_data[i], 0)
        results = sorted([(score, index) for (index, score) in d_list.items()], reverse=True)
        return results[0:3]
