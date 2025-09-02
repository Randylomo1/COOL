from django.urls import path
from . import views

urlpatterns = [
    path('', views.livestock_list, name='livestock_list'),
    path('add/', views.livestock_add, name='livestock_add'),
]
