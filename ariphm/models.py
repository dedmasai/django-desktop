from django.db import models
from django.contrib.auth.models import User


class Variant(models.Model):
    number=models.IntegerField(default=0)
    theme=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(null=False, blank=True)
    answer=models.IntegerField(default=0)
   # variants=models.ManyToManyField(Variant,related_name="tasks")

    def __str__(self):
        return f"Задание(pk={self.pk}, название= {self.name!r})"

class taskList(models.Model):
    varNumber=models.IntegerField(default=0)
    number=models.IntegerField(default=0)
    text=models.TextField(null=False, blank=True)
    answer=models.IntegerField(default=0)
    succ=models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class quiz(models.Model):
    #date=models.DateTimeField(auto_now_add=True)
    #taskId = models.ForeignKey(taskList,on_delete=models.PROTECT)
    #userID = models.ForeignKey(User, on_delete=models.PROTECT)
    number = models.IntegerField(default=0)
    uAnswer = models.IntegerField(default=0)
    succ = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Задание(pk={self.pk}, название= {self.name!r})"
class AnswerQuiz(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    numb = models.IntegerField(default=0)
    uAns = models.IntegerField(default=0)
    suc = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Задание(pk={self.pk}, название= {self.name!r})"