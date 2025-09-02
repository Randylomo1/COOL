from django.shortcuts import render, redirect
from .models import Yield
from .forms import YieldForm

def yield_list(request):
    yields = Yield.objects.all()
    return render(request, 'yield/yield_list.html', {'yields': yields})

def yield_add(request):
    if request.method == 'POST':
        form = YieldForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('yield_list')
    else:
        form = YieldForm()
    return render(request, 'yield/yield_form.html', {'form': form})
