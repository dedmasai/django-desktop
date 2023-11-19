from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpRequest
from django.urls import path

from .views import (
    AboutMeView,
    register_page,
    welcome,
    MyLogoutView,
    RegisterView
)

app_name = "myauth"

urlpatterns = [

    path("", welcome, name="welcome"),
    path("logout/", MyLogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("about-me/", AboutMeView.as_view(), name="about-me"),
    path("login/", LoginView.as_view(template_name='myauth/login.html',
                                     redirect_authenticated_user=True), name="login"),

]