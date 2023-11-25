from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpRequest
from django.urls import path

from .views import (
    quiz,
    results,
    journal
)

app_name = "quiz"

urlpatterns = [
    path("journal", journal, name="journ"),
    path("res", results, name="res"),
    path("", quiz, name="quiz"),
]