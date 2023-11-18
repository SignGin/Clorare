from django.urls import path
from .views import ClothesView, ClothesDetailView, ClothesRecommendationView

app_name = 'clothes'

urlpatterns = [
    # 옷 목록 조회, 추가
    path('', ClothesView.as_view()),
    # 특정 옷 조회, 수정, 삭제
    path('<int:pk>/', ClothesDetailView.as_view()),
    # 옷 랜덤 추천
    path('reco/<int:gender>/', ClothesRecommendationView.as_view()),
]
