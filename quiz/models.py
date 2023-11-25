from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    taskID = models.ForeignKey(Task, on_delete=models.PROTECT, null=True)
    userID=models.ForeignKey(User,on_delete=models.PROTECT, null=True)


class VClass(models.Model):
    name=models.TextField(null=True, blank=True)
    gender=models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name

class Work(models.Model):
    name=models.TextField(null=True, blank=True)
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sClass = models.ForeignKey(VClass,on_delete=models.PROTECT, null=True)
    workToDo=models.ManyToManyField(Work,blank=True,related_name='student')
    gender=models.CharField(max_length=10,null=True, blank=True)
    mark=models.FloatField(null=True, blank=True)
    def __str__(self):
        return self.user.first_name+' '+self.user.last_name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.student.save()



