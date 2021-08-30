from django.urls import path
from users.views import UserResigtrationView, activate_user
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', UserResigtrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name="users/login.html"), name='login'),
    path('active/<ub64>/<token>/', activate_user, name='activate'),
]
