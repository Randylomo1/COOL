from django.shortcuts import render

def weather_list(request):
    return render(request, 'weather/weather_list.html')
