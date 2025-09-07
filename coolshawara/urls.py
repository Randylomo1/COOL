from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/signup/', views.signup_view, name='signup'),
    path('', include('apps.accounts.urls')),
    path('', include('apps.crops.urls')),
    path('', include('apps.dashboard.urls')),
    path('', include('apps.finance.urls')),
    path('', include('apps.incidents.urls')),
    path('', include('apps.inventory.urls')),
    path('', include('apps.livestock.urls')),
    path('', include('apps.locations.urls')),
    path('', include('apps.reports.urls')),
    path('', include('apps.timelogs.urls')),
    path('', include('apps.weather.urls')),
    path('', include('apps.workers.urls')),
    path('', include('apps.yield.urls')),
]