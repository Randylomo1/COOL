from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from apps.accounts.forms import CustomUserCreationForm
from django.db.models import Sum
from apps.crops.models import Crop
from apps.livestock.models import Livestock
from apps.inventory.models import InventoryItem
from apps.finance.models import Finance
from apps.workers.models import Worker

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    total_crops = Crop.objects.count()
    total_livestock = Livestock.objects.count()
    total_inventory = InventoryItem.objects.count()
    total_workers = Worker.objects.count()

    income = Finance.objects.filter(type='income').aggregate(total=Sum('amount'))['total'] or 0
    expenses = Finance.objects.filter(type='expense').aggregate(total=Sum('amount'))['total'] or 0
    net_profit = income - expenses

    financials = {
        'income': income,
        'expenses': expenses,
        'net_profit': net_profit,
    }

    context = {
        'total_crops': total_crops,
        'total_livestock': total_livestock,
        'total_inventory': total_inventory,
        'total_workers': total_workers,
        'income': income,
        'expenses': expenses,
        'net_profit': net_profit,
        'financials': financials,
    }
    return render(request, 'dashboard/dashboard.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
