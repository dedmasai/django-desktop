from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    varNumber=models.IntegerField(default=0)
    number=models.IntegerField(default=0)
    text=models.TextField(null=False, blank=True)
    answer=models.IntegerField(default=0)
    rightAnswCount=models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    isSubmitted = models.BooleanField(default=False)

class AnswerQuiz(models.Model):
    taskN = models.IntegerField(default=0)
    userN = models.IntegerField(default=0)
    numbInV = models.IntegerField(default=0)
    uAnswer = models.IntegerField(default=0)
    correct = models.BooleanField(default=False)
    isSubmitted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    correctAns=models.IntegerField(default=0)
    textAns=models.TextField(null=True, blank=True)