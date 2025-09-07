from django.urls import path
from . import views

urlpatterns = [
    path('', views.locations_list, name='locations_list'),
]
