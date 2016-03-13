from __future__ import print_function
from django.shortcuts import render
from .forms import IMGForm
from .models import IMGFile
from .helper import create_histogram
import sys


def home(request):
    if request.method == 'POST':
        form = IMGForm(request.POST, request.FILES)
        if form.is_valid():
            new_img = IMGFile(imgFile=request.FILES['imgField'])
            new_img.save()
            csv_data = create_histogram(new_img.pk)
            results = []
            print('in POST method for index: ', new_img.csv_index, end='\n', file=sys.stdout.flush())
            for (score, index) in csv_data:
                results.append((IMGFile.objects.get(csv_index=index), str(score)))
                print(index, score, sep=', ', end='\n', file=sys.stdout.flush())
            new_form = IMGForm()
            return render(request, 'home.html', {'form': new_form, 'picture': new_img, 'images': results})
    else:
        form = IMGForm()
        print('NOT in POST method...', end='\n', file=sys.stdout.flush())
    return render(request, 'home.html', {'form': form, 'images': []})

