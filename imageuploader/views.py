from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import IMGFile
from .forms import IMGForm
from django.shortcuts import render_to_response, render
from django.template import RequestContext
import cv2
import


def index(request):
    return render('base.html')


def upload_file(request):
    if request.method == 'POST':
        form = IMGForm(request.POST, request.FILES)
        if form.is_valid():
            newImg = IMGFile(imgFile=request.FILES['imgField'])
            newImg.save()
            dict = {'imgResult': IMGFile.objects.get(id=newImg.id), 'form': form}
            #return HttpResponseRedirect(reverse('upload_file'))
    else:
        form = IMGForm()
        dict = {'form': form}
    return render_to_response('base.html', dict, context_instance=RequestContext(request))
