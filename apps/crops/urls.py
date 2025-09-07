from django.urls import path
from . import views

urlpatterns = [
    path('', views.crop_list, name='crop_list'),
    path('<int:pk>/', views.crop_detail, name='crop_detail'),
    path('add/', views.crop_add, name='crop_add'),
    path('<int:pk>/update/', views.crop_update, name='crop_update'),
    path('<int:pk>/delete/', views.crop_delete, name='crop_delete'),
]
