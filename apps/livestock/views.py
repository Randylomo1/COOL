from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Livestock
from .forms import LivestockForm

@login_required
def livestock_list(request):
    livestock = Livestock.objects.all()
    return render(request, 'livestock/livestock_list.html', {'livestock': livestock})

@login_required
def livestock_detail(request, pk):
    animal = get_object_or_404(Livestock, pk=pk)
    return render(request, 'livestock/livestock_detail.html', {'animal': animal})

@login_required
def livestock_add(request):
    if request.method == 'POST':
        form = LivestockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livestock_list')
    else:
        form = LivestockForm()
    return render(request, 'livestock/livestock_form.html', {'form': form})

@login_required
def livestock_update(request, pk):
    animal = get_object_or_404(Livestock, pk=pk)
    if request.method == 'POST':
        form = LivestockForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('livestock_list')
    else:
        form = LivestockForm(instance=animal)
    return render(request, 'livestock/livestock_form.html', {'form': form})

@login_required
def livestock_delete(request, pk):
    animal = get_object_or_404(Livestock, pk=pk)
    if request.method == 'POST':
        animal.delete()
        return redirect('livestock_list')
    return render(request, 'livestock/livestock_confirm_delete.html', {'animal': animal})
