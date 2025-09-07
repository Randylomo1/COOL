from django.shortcuts import render

def yield_list(request):
    return render(request, 'yield/yield_list.html')
