from django.contrib import admin
from django.urls import path, include
from restapi import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('weatherdata/', views.request_api),
    path('weatherdata/<int:pk>/', views.request_cloth),
    path('weatherdata/reco/<int:sex>/', views.request_reco),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
