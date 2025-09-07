from django.shortcuts import render

def timelogs_list(request):
    return render(request, 'timelogs/timelogs_list.html')
