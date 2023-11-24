from django.core.management import BaseCommand
from quiz.models import Task, AnswerQuiz

from random import randint, shuffle
class Command(BaseCommand):
    def handle(self, *args, **options):
        ao=AnswerQuiz.objects.all()
        to=Task.objects.all()
        for a in ao:
            t=to.filter(pk=a.taskN)
            a.textAns=t[0].text
            a.correctAns=t[0].answer
            a.save()



