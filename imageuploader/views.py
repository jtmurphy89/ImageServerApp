from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import IMGFile
from .forms import IMGForm
from django.shortcuts import render_to_response
from django.template import RequestContext


def upload_file(request):
    if request.method == 'POST':
        form = IMGForm(request.POST, request.FILES)
        if form.is_valid():
            newImg = IMGFile(imgFile=request.FILES['imgFile'])
            newImg.save()
            return HttpResponseRedirect(reverse('upload_file'))
    else:
        form = IMGForm()
    return render(request, 'base.html', {'form': form})
