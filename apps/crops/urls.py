from django.urls import path
from . import views

urlpatterns = [
    path('', views.crop_list, name='crop_list'),
    path('add/', views.crop_add, name='crop_add'),
]
