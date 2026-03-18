from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('users/', views.UserListCreateView.as_view(), name='user'),
    path('users/<int:pk>/', views.UserRetrieveUpdateView.as_view(), name='user-detail'),
]