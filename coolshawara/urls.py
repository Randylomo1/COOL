from django.contrib import admin
from django.urls import path, include
from . import views
from allauth.account import views as allauth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.splash, name='splash'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    
    # Allauth URLs
    path('accounts/', include('allauth.urls')),
    
    # Local App URLs
    path('dashboard/', include('apps.dashboard.urls')),
    path('crops/', include('apps.crops.urls')),
    path('finance/', include('apps.finance.urls')),
    path('incidents/', include('apps.incidents.urls')),
    path('inventory/', include('apps.inventory.urls')),
    path('livestock/', include('apps.livestock.urls')),
    path('locations/', include('apps.locations.urls')),
    path('reports/', include('apps.reports.urls')),
    path('timelogs/', include('apps.timelogs.urls')),
    path('weather/', include('apps.weather.urls')),
    path('workers/', include('apps.workers.urls')),
    path('yield/', include('apps.yield.urls')),
    path('users/', include('apps.users.urls')),
]
