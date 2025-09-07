from django.shortcuts import render

def locations_list(request):
    return render(request, 'locations/locations_list.html')
