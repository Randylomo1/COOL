from django.urls import path
from . import views

urlpatterns = [
    path('', views.incidents_list, name='incidents_list'),
    path('new/', views.incident_create, name='incident_create'),
    path('<int:pk>/edit/', views.incident_update, name='incident_update'),
    path('<int:pk>/delete/', views.incident_delete, name='incident_delete'),
]
