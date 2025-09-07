from django.shortcuts import render

def incidents_list(request):
    return render(request, 'incidents/incidents_list.html')
