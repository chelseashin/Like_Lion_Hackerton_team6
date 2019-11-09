from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/profile_id', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('mypage/<str:profile_id>', views.mypage, name="mypage"),
]