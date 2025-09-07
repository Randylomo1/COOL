from django.urls import path
from . import views

urlpatterns = [
    path('', views.timelogs_list, name='timelogs_list'),
]
