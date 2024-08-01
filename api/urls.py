from os import name

from django.urls import path

from api.views import UserDetailAPIVIew, UserListAPIView

app_name = 'api'

urlpatterns = [
    path('users/<int:id>/', UserDetailAPIVIew.as_view(), name='user-detail'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
]
