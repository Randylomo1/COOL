from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def locations_list(request):
    return render(request, 'locations/locations_list.html')
