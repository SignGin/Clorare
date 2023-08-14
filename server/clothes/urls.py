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
    # path('reco/', views.ClothesRecommendation.as_view(), name='reco'),
]
