from django.core.management import BaseCommand
from quiz.models import Task, AnswerQuiz, Student, VClass
from django.contrib.auth.models import User

from random import randint, shuffle
class Command(BaseCommand):
    def handle(self, *args, **options):
        VClass.objects.get_or_create(name='5a', gender='m')
        VClass.objects.get_or_create(name='5b', gender='f')



