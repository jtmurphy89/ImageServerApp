from django.db import models
from time import time


def generate_filename(instance, filename):
    ext = filename.split('.')[-1]
    return str(int(time())) + '.' + ext


class IMGFile(models.Model):
    imgFile = models.ImageField(upload_to=generate_filename)
    csv_index = models.IntegerField(default=0)

