from django.urls import path
from . import views

urlpatterns = [
    path('', views.yield_list, name='yield_list'),
]
