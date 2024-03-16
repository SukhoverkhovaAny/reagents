from django.core.management.base import BaseCommand
from reagents.models import Reagent


class Command(BaseCommand):
    help = "Get reagent by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Reagent ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        reagent = Reagent.objects.filter(pk=pk).first()
        self.stdout.write(f'{reagent}')