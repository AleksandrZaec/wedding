from django.urls import path
from .views import UserCreateAPIView, UserListAPIView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, )

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create/', UserCreateAPIView.as_view(), name='user-create'),
    path('list/', UserListAPIView.as_view(), name='user-list'),
]