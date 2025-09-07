from django.shortcuts import render, redirect, get_object_or_404
from .models import Worker
from .forms import WorkerForm

def worker_list(request):
    workers = Worker.objects.all()
    return render(request, 'workers/worker_list.html', {'workers': workers})

def worker_detail(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    return render(request, 'workers/worker_detail.html', {'worker': worker})

def worker_add(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('worker_list')
    else:
        form = WorkerForm()
    return render(request, 'workers/worker_form.html', {'form': form})

def worker_update(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    if request.method == 'POST':
        form = WorkerForm(request.POST, instance=worker)
        if form.is_valid():
            form.save()
            return redirect('worker_list')
    else:
        form = WorkerForm(instance=worker)
    return render(request, 'workers/worker_form.html', {'form': form})

def worker_delete(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    if request.method == 'POST':
        worker.delete()
        return redirect('worker_list')
    return render(request, 'workers/worker_confirm_delete.html', {'worker': worker})
