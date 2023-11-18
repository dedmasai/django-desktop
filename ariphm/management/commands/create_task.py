from django.core.management import BaseCommand
from ariphm.models import Task
class Command(BaseCommand):
    def handle(self, *args, **options):

        task_names=[
            "Сложение",
            "Вычитание",
            "Умножение",
            "Деление",
        ]
        for task_name in task_names:
            task, craeted= Task.objects.get_or_create(name=task_name)
            self.stdout.write(f"Created task {task.name}")