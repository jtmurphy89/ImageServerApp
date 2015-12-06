from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import IMGFile
from .forms import IMGForm
from django.shortcuts import render_to_response, render
from django.template import RequestContext


# from helper import histHelper

def upload_file(request):
    if request.method == 'POST':
        form = IMGForm(request.POST, request.FILES)
        if form.is_valid():
            newImg = IMGFile(imgFile=request.FILES['imgField'])
            newImg.save()
            # create new histogram using helper and save it to histograms folder
            return HttpResponseRedirect(reverse('upload_file'))
            # return HTTPResponseRedirect(os.path.join(BASE_DIR, 'imageUploader/results', newImg.url)
    else:
        form = IMGForm()
    return render_to_response('base.html', {'form': form}, context_instance=RequestContext(request))


# will call histHelper.histCompare and render its output in basic.html
# def results(request, imagename):
#     return render('base.html')
