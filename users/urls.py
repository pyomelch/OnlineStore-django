from django.urls import path
from django.contrib.auth.decorators import login_required

from users.views import login, UserRegistrationView, logout, UserProfileView

app_name = "users"

urlpatterns = [
    path("login/", login, name="login"),  # users/login
    path("registration/", UserRegistrationView.as_view(), name="registration"),  # users/registration
    path("profile/<int:pk>/", login_required(UserProfileView.as_view()), name="profile"),  # users/profile
    path("logout/", logout, name="logout"),  # users/logout
]
