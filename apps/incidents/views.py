from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Incident
from .forms import IncidentForm

@login_required
def incidents_list(request):
    incidents = Incident.objects.filter(reported_by=request.user)
    return render(request, 'incidents/incidents_list.html', {'incidents': incidents})

@login_required
def incident_create(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            incident = form.save(commit=False)
            incident.reported_by = request.user
            incident.save()
            return redirect('incidents_list')
    else:
        form = IncidentForm()
    return render(request, 'incidents/incident_form.html', {'form': form})

@login_required
def incident_update(request, pk):
    incident = get_object_or_404(Incident, pk=pk, reported_by=request.user)
    if request.method == 'POST':
        form = IncidentForm(request.POST, instance=incident)
        if form.is_valid():
            form.save()
            return redirect('incidents_list')
    else:
        form = IncidentForm(instance=incident)
    return render(request, 'incidents/incident_form.html', {'form': form})

@login_required
def incident_delete(request, pk):
    incident = get_object_or_404(Incident, pk=pk, reported_by=request.user)
    if request.method == 'POST':
        incident.delete()
        return redirect('incidents_list')
    return render(request, 'incidents/incident_confirm_delete.html', {'incident': incident})
