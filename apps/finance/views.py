from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Finance
from .forms import FinanceForm

@login_required
def finance_list(request):
    finances = Finance.objects.all()
    return render(request, 'finance/finance_list.html', {'finances': finances})

@login_required
def finance_detail(request, pk):
    finance = get_object_or_404(Finance, pk=pk)
    return render(request, 'finance/finance_detail.html', {'finance': finance})

@login_required
def finance_create(request):
    if request.method == 'POST':
        form = FinanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finance_list')
    else:
        form = FinanceForm()
    return render(request, 'finance/finance_form.html', {'form': form})

@login_required
def finance_update(request, pk):
    finance = get_object_or_404(Finance, pk=pk)
    if request.method == 'POST':
        form = FinanceForm(request.POST, instance=finance)
        if form.is_valid():
            form.save()
            return redirect('finance_list')
    else:
        form = FinanceForm(instance=finance)
    return render(request, 'finance/finance_form.html', {'form': form})

@login_required
def finance_delete(request, pk):
    finance = get_object_or_404(Finance, pk=pk)
    if request.method == 'POST':
        finance.delete()
        return redirect('finance_list')
    return render(request, 'finance/finance_confirm_delete.html', {'finance': finance})
