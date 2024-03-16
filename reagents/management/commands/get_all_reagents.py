from django.core.management.base import BaseCommand
from reagents.models import Reagent


class Command(BaseCommand):
    help = "Get all reagents."

    def handle(self, *args, **kwargs):
        reagents = Reagent.objects.all()
        self.stdout.write(f'{reagents}')