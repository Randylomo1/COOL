from django.shortcuts import render, redirect, get_object_or_404
from .models import Crop
from .forms import CropForm

def crop_list(request):
    crops = Crop.objects.all()
    return render(request, 'crops/crop_list.html', {'crops': crops})

def crop_detail(request, pk):
    crop = get_object_or_404(Crop, pk=pk)
    return render(request, 'crops/crop_detail.html', {'crop': crop})

def crop_add(request):
    if request.method == 'POST':
        form = CropForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crop_list')
    else:
        form = CropForm()
    return render(request, 'crops/crop_form.html', {'form': form})

def crop_update(request, pk):
    crop = get_object_or_404(Crop, pk=pk)
    if request.method == 'POST':
        form = CropForm(request.POST, instance=crop)
        if form.is_valid():
            form.save()
            return redirect('crop_list')
    else:
        form = CropForm(instance=crop)
    return render(request, 'crops/crop_form.html', {'form': form})

def crop_delete(request, pk):
    crop = get_object_or_404(Crop, pk=pk)
    if request.method == 'POST':
        crop.delete()
        return redirect('crop_list')
    return render(request, 'crops/crop_confirm_delete.html', {'crop': crop})
