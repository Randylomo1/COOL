from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def weather_list(request):
    return render(request, 'weather/weather_list.html')
