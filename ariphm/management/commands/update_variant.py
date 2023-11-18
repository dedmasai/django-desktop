from django.core.management import BaseCommand
from ariphm.models import Variant,Task
class Command(BaseCommand):
    def handle(self, *args, **options):
        tasks=Task.objects.all()
        variant=Variant.objects.first()

        for task in tasks:
            variant.tasks.add(task)

        variant.save()

        self.stdout.write(self.style.SUCCESS(f"Successfully added tasks {variant.tasks.all()} to variant {variant}"))