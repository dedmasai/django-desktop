from django.contrib.auth.models import User
from django.core.management import BaseCommand
from quiz.models import Task, Work

from random import randint, shuffle
class Command(BaseCommand):
    def handle(self, *args, **options):
        w,c=Work.objects.get_or_create(name="Деление",numbOfTasks=5)
        for v in User.objects.all():
            v.student.workToDo.add(w)
            for n in range(12,13):
                c = randint(2, 10)
                b = c*randint(2, 10)
                a = randint(50, 100)
                d = (a *b)// c
                text=f"Сосчитайте удобным способом ({a} х {b}):{c}. "
                Task.objects.create(varNumber=v.pk,toUser=v,work=w,number=n,text=text,answer=d)
            for n in range(13,14):
                d = 20
                text=f"Сосчитайте удобным способом (8 х 25):10. "
                Task.objects.create(varNumber=v.pk,toUser=v,work=w,number=n,text=text,answer=d)
            for n in range(14,15):
                c = randint(2, 10)
                b = c*randint(2, 10)
                a = randint(50, 100)
                d = (b *a)// c
                text=f"Сосчитайте удобным способом ({a} х {b}):{c}. "
                Task.objects.create(varNumber=v.pk,toUser=v,work=w,number=n,text=text,answer=d)

            for n in range(15,16):
                c = randint(2, 10)
                b = c*randint(2, 10)
                a = b*randint(5, 20)
                d = a //(b* c)
                text=f"Решите удобным способом {a} : ({b} x {c}). "
                Task.objects.create(varNumber=v.pk,toUser=v,work=w,number=n,text=text,answer=d)
            for n in range(16, 17):
                c = randint(2, 10)
                b = randint(2, 10)
                a = c * b*randint(10, 20)
                d = a // (b * c)
                text = f"Решите удобным способом {a} : ({c} x {b}). "
                Task.objects.create(varNumber=v.pk, toUser=v, work=w, number=n, text=text, answer=d)

