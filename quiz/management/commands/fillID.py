from django.core.management import BaseCommand
from quiz.models import Task, AnswerQuiz
from django.contrib.auth.models import User

from random import randint, shuffle
class Command(BaseCommand):
    def handle(self, *args, **options):
        ao=AnswerQuiz.objects.all()
        for a in ao:
            a.userID=User.objects.get(pk=a.userN)
            a.taskID=Task.objects.get(pk=a.taskN)
            a.save()



