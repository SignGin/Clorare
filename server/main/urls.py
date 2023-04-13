from django.contrib import admin
from django.urls import path, include, re_path
from restapi import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
    openapi.Info(
        title="Cloth Random Recommendation",
        default_version='v1.1',
        description="# 오늘 날씨에 따라 랜덤으로 옷을 추천해드립니다.",
        terms_of_service="",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    # swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # django
    path('admin/', admin.site.urls),
    path('weatherdata/', views.request_api),
    path('weatherdata/<int:pk>/', views.request_cloth),
    path('weatherdata/reco/<int:sex>/', views.request_reco),
    path('weatherdata/w-data/', views.request_weather),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
