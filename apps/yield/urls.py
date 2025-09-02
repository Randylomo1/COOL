from django.urls import path
from . import views

urlpatterns = [
    path('', views.yield_list, name='yield_list'),
    path('add/', views.yield_add, name='yield_add'),
]
