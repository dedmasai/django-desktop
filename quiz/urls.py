from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpRequest
from django.urls import path

from .views import (
    quiz,
    results,
)

app_name = "quiz"

urlpatterns = [
    path("res", results, name="res"),
    path("", quiz, name="quiz"),
]