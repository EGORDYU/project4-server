from django.urls import path
from . import views
from .views import UserCreateView, UserProfileView, TokenRefreshView


urlpatterns = [
    path('home/', views.HomeView.as_view(), name ='home'),
    path('logout/', views.LogoutView.as_view(), name ='logout'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
     path('api/user/profile/', UserProfileView.as_view(), name='user-profile'),
     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]