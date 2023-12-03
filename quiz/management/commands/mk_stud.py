from django.core.management import BaseCommand
from quiz.models import Task, AnswerQuiz, Student, VClass
from django.contrib.auth.models import User

from random import randint, shuffle
class Command(BaseCommand):
    def handle(self, *args, **options):
        sts = Student.objects.all()
        us = User.objects.all()
        for u in us:
            Student.objects.create(user=u)



