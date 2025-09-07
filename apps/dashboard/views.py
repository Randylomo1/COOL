from django.shortcuts import render
from django.db.models import Sum
from apps.crops.models import Crop
from apps.livestock.models import Livestock
from apps.inventory.models import InventoryItem
from apps.finance.models import Finance
from apps.workers.models import Worker

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
