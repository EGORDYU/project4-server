from django.urls import path
from . import views
from .views import UserCreateView


urlpatterns = [
    path('home/', views.HomeView.as_view(), name ='home'),
    path('logout/', views.LogoutView.as_view(), name ='logout'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
]