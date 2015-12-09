from .forms import IMGForm
from .models import IMGFile
from django.shortcuts import render, redirect


# from helper import histHelper

def home(request):
    if request.method == 'POST':
        form = IMGForm(request.POST, request.FILES)
        if form.is_valid():
            newimg = IMGFile(imgFile=request.FILES['imgField'])
            newimg.save()
            # create new histogram using helper and save it to histograms folder
            return redirect('/')
            # return HTTPResponseRedirect(os.path.join(BASE_DIR, 'imageUploader/results', newImg.url)
    else:
        form = IMGForm()
    images = IMGFile.objects.all()
    return render(request, 'home.html', {'form': form, 'images': images})


# will call histHelper.histCompare and render its output in basic.html
# def results(request, imagename):
#     return render('_base.html')
