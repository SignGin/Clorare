"""
URL configuration for clorare_server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

app_name = 'clothes'

urlpatterns = [
    # 옷 목록 조회
    path('', views.ClothesList.as_view(), name='list'),
    # 특정 번호의 옷 오브젝트 조회
    path('<int:pk>/', views.ClothesDetail.as_view(), name='delete'),
    # 특정 번호의 옷 오브젝트 삭제
    path('delete/<int:pk>/', views.ClothesDelete.as_view(), name='delete'),
    # 모델에 옷 오브젝트 추가
    path('add/', views.ClothesAdd.as_view(), name='add'),
    # 옷 랜덤 추천
    # path('recp/', views.ClothesRecommendation.as_view(), name='reco'),


    # path('update/<int:pk>/', views.ClothesUpdate.as_view(), name='update'),
]
