from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import InventoryItem
from .forms import InventoryItemForm

@login_required
def inventory_item_list(request):
    items = InventoryItem.objects.all()
    return render(request, 'inventory/inventory_item_list.html', {'items': items})

@login_required
def inventory_item_detail(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    return render(request, 'inventory/inventory_item_detail.html', {'item': item})

@login_required
def inventory_item_create(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_item_list')
    else:
        form = InventoryItemForm()
    return render(request, 'inventory/inventory_item_form.html', {'form': form})

@login_required
def inventory_item_update(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    if request.method == 'POST':
        form = InventoryItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('inventory_item_list')
    else:
        form = InventoryItemForm(instance=item)
    return render(request, 'inventory/inventory_item_form.html', {'form': form})

@login_required
def inventory_item_delete(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('inventory_item_list')
    return render(request, 'inventory/inventory_item_confirm_delete.html', {'item': item})
