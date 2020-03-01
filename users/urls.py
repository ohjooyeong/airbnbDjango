"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login"),
    path('login/github/', views.github_login, name="github-login"),
    path('login/github/callback/', views.github_callback, name="github-callback"),
    path('login/kakao/', views.kakao_login, name="kakao-login"),
    path('login/kakao/callback/', views.kakao_callback, name="kakao-callback"),
    path('logout/', views.log_out, name="logout"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('verify/<str:key>/', views.complete_verification, name="complete-verification"),
    path('update-profile/', views.UpdateProfileView.as_view(), name="update"),
    path('update-password/', views.UpdatePasswordView.as_view(), name="password"),
    path('<int:pk>/', views.UserProfileView.as_view(), name="profile"),
    path('switch-hosting/', views.switch_hosting, name="switch-hosting"),
]
