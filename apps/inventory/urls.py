from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_item_list, name='inventory_item_list'),
    path('<int:pk>/', views.inventory_item_detail, name='inventory_item_detail'),
    path('new/', views.inventory_item_create, name='inventory_item_create'),
    path('<int:pk>/edit/', views.inventory_item_update, name='inventory_item_update'),
    path('<int:pk>/delete/', views.inventory_item_delete, name='inventory_item_delete'),
]
