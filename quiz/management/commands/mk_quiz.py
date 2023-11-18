from django.core.management import BaseCommand
from quiz.models import Task

from random import randint, shuffle
class Command(BaseCommand):
    def handle(self, *args, **options):
        varN=200
        for v in range(varN):
            n = 1
            b = randint(11, 99)
            a = b * randint(1, 10000)
            d = a // b
            text=f"Сколько будет {a} разделить на {b}?"
            task, craeted= Task.objects.get_or_create(varNumber=v,number=n,text=text,answer=d)
            self.stdout.write(f"Created task {task.text}")

            n = 2
            b = randint(5, 20) * 10 ** randint(1, 3)
            a = b * randint(1, 100) * 10 ** randint(1, 2)
            d = a // b
            text = f"Сколько будет {a} разделить на {b}?"
            task, craeted = Task.objects.get_or_create(varNumber=v, number=n, text=text, answer=d)
            self.stdout.write(f"Created task {task.text}")

            n = 3
            b = randint(1, 999)
            a = randint(0, 9) * 1000 + b
            c = randint(0, b)
            d = a - (b - c)
            text = f"Сколько будет {a} разделить на {b}?"
            task, craeted = Task.objects.get_or_create(varNumber=v, number=n, text=text, answer=d)
            self.stdout.write(f"Created task {task.text}")