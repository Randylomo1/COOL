from django.urls import path
from . import views

urlpatterns = [
    path('', views.worker_list, name='worker_list'),
    path('<int:pk>/', views.worker_detail, name='worker_detail'),
    path('add/', views.worker_add, name='worker_add'),
    path('<int:pk>/update/', views.worker_update, name='worker_update'),
    path('<int:pk>/delete/', views.worker_delete, name='worker_delete'),
]
