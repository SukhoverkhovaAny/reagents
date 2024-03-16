from django.core.management.base import BaseCommand
from reagents.models import Reagent


class Command(BaseCommand):
    help = "Delete reagent by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Reagent ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        reagent = Reagent.objects.filter(pk=pk).first()
        if reagent is not None:
            reagent.delete()
        self.stdout.write(f'{reagent} removed')