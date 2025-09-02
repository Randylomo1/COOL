from django.shortcuts import render, redirect
from .models import Crop
from .forms import CropForm

def crop_list(request):
    crops = Crop.objects.all()
    return render(request, 'crops/crop_list.html', {'crops': crops})

def crop_add(request):
    if request.method == 'POST':
        form = CropForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crop_list')
    else:
        form = CropForm()
    return render(request, 'crops/crop_form.html', {'form': form})
