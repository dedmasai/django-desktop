from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpRequest
from django.urls import path

from .views import (
    quiz
)

app_name = "quiz"

urlpatterns = [
    path("", quiz, name="quiz"),
]