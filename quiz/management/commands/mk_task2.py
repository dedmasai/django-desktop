from django.contrib.auth.models import User
from django.core.management import BaseCommand
from quiz.models import Task, Work

from random import randint, shuffle
class Command(BaseCommand):
    def handle(self, *args, **options):
        Work.objects.create(name="Простые упражнения")
        w=Work.objects.get(pk=1)
        for v in User.objects.all():
            for n in range(1,3):
                b = randint(2, 15)
                a = b * randint(3, 30)
                d = a // b
                text=f"Сколько будет {a} разделить на {b}?"
                Task.objects.create(varNumber=v.pk,toUser=v,work=w,number=n,text=text,answer=d)


            for n in range(3,6):
                b = randint(5, 20)
                a = randint(3, 20)
                d = a * b
                text = f"Сколько будет {a} умножить на {b}?"
                Task.objects.create(varNumber=v.pk,toUser=v,work=w,number=n,text=text,answer=d)


            for n in range(6,9):
                b = randint(22, 77)
                a = randint(33, 88)
                c = randint(0, b)
                d = a +b
                text = f"Что будет результатом сложения {a} и {b}?"
                Task.objects.create(varNumber=v.pk,toUser=v,work=w,number=n,text=text,answer=d)

            for n in range(9,12):
                b = randint(22, 77)
                a = b+randint(33, 88)
                c = randint(0, b)
                d = a -b
                text = f"Чему будет равна разность чисел {a} и {b}?"
                Task.objects.create(varNumber=v.pk,toUser=v,work=w,number=n,text=text,answer=d)
