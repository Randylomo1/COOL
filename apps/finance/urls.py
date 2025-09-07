from django.urls import path
from . import views

urlpatterns = [
    path('', views.finance_list, name='finance_list'),
    path('<int:pk>/', views.finance_detail, name='finance_detail'),
    path('new/', views.finance_create, name='finance_create'),
    path('<int:pk>/edit/', views.finance_update, name='finance_update'),
    path('<int:pk>/delete/', views.finance_delete, name='finance_delete'),
]
