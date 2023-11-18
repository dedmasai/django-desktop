from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpRequest
from django.urls import path

from .views import (
    task_list,
    quiz
)

app_name = "ariphm"

urlpatterns = [
    path("tasks/", task_list, name="task_list"),
    path("quiz/", quiz, name="quiz"),
]