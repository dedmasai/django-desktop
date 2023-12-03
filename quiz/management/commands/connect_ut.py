from django.core.management import BaseCommand
from quiz.models import Task, AnswerQuiz
from django.contrib.auth.models import User
from random import randint, shuffle
class Command(BaseCommand):
    def handle(self, *args, **options):
        ao=AnswerQuiz.objects.all()
        to=Task.objects.all()
        for a in ao:
            t=to.filter(pk=a.taskN).first()
            u=User.objects.filter(pk=a.userN).first()
            a.userID=u
            a.taskID=t
            a.save()



