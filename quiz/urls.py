from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpRequest
from django.urls import path

from .views import (
    quiz,
    results,
    journal,
    work,
    mainJournal
)

app_name = "quiz"

urlpatterns = [
    path("work_journal", mainJournal, name="main_journal"),
    path("work", work, name="work"),
    path("journal", journal, name="journ"),
    path("res", results, name="res"),
    path("", quiz, name="quiz"),
]