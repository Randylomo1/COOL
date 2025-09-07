from django.urls import path
from . import views

urlpatterns = [
    path('', views.livestock_list, name='livestock_list'),
    path('<int:pk>/', views.livestock_detail, name='livestock_detail'),
    path('add/', views.livestock_add, name='livestock_add'),
    path('<int:pk>/edit/', views.livestock_update, name='livestock_update'),
    path('<int:pk>/delete/', views.livestock_delete, name='livestock_delete'),
]
