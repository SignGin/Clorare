from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clothes/', include('clothes.urls')),
    path('weather/', include('openweather.urls'))
]
