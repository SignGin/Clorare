from django.urls import include, path
from rest_framework import routers
from restapi import views


router = routers.DefaultRouter()
# router.register(r'analysis', views.AnalysisViewSet)
router.register(r'clothes', views.ClothesViewSet)
router.register(r'reco', views.Recommendation)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]