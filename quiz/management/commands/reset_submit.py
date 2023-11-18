from django.core.management import BaseCommand
from quiz.models import Task

from random import randint, shuffle
class Command(BaseCommand):
    def handle(self, *args, **options):
        to=Task.objects.filter(isSubmitted=True)
        for t in to:
            t.isSubmitted=False
            t.save()
