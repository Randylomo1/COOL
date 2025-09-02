from django.shortcuts import render, redirect
from .models import Livestock
from .forms import LivestockForm

def livestock_list(request):
    livestock = Livestock.objects.all()
    return render(request, 'livestock/livestock_list.html', {'livestock': livestock})

def livestock_add(request):
    if request.method == 'POST':
        form = LivestockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livestock_list')
    else:
        form = LivestockForm()
    return render(request, 'livestock/livestock_form.html', {'form': form})
