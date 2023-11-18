from django.core.management import BaseCommand
from ariphm.models import Variant
class Command(BaseCommand):
    def handle(self, *args, **options):
        numbers=[
            1,
            3,
            14,
            7,
        ]
        for number in numbers:
            variant, craeted= Variant.objects.get_or_create(number=number)
            self.stdout.write(f"Created variant {variant.number}")