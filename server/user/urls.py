from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView
from .views import RegistrationView, UserLoginView


urlpatterns = [
    # user
    path('register/', RegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),

    # jwt
    path('token/', TokenObtainPairView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
