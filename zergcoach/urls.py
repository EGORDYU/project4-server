from django.urls import path
from . import views
from .views import UserCreateView, UserProfileView, TokenRefreshView
from .views import FavoriteView, DeleteFavoriteView, UserFavoritesView

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('api/user/profile/', UserProfileView.as_view(), name='user-profile'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('favorites/', FavoriteView.as_view(), name='favorites'),
    path('api/favorites/list/', UserFavoritesView.as_view(), name='user-favorites'),
    path('favorites/<int:build_order_id>/delete/', DeleteFavoriteView.as_view(), name='delete-favorite'),
    path('api/builds/<int:build_id>/', views.BuildDetailView.as_view(), name='build-detail'),
]
