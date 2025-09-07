from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('finance/', include('apps.finance.urls')),
    path('inventory/', include('apps.inventory.urls')),
]
