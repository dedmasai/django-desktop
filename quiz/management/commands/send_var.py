from django.contrib.auth.models import User
from django.core.management import BaseCommand
from quiz.models import Task, Work, Student

from random import randint, shuffle
class Command(BaseCommand):
    def handle(self, *args, **options):
        w=Work.objects.first()
        w.student.set(Student.objects.all())
