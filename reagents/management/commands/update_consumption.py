from django.core.management.base import BaseCommand
from reagents.models import Reagent
import logging

logger = logging.getLogger(__name__)
FORMAT = '{asctime:20} - {levelname:10} - "{name}" : {msg}'
logging.basicConfig(format=FORMAT, style='{', filename='log/django.log', filemode='a',
                    level=logging.INFO)


class Command(BaseCommand):
    help = "Update reagent consumption by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Reagent ID')
        parser.add_argument("new_date_of_consumption", type=str, help="Reagent date of consumption")
        parser.add_argument("new_quantity_of_consumption", type=float, help="Reagent quantity of consumption")

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        new_date_of_consumption = kwargs.get('new_date_of_consumption')
        new_quantity_of_consumption = kwargs.get('new_quantity_of_consumption')
        reagent = Reagent.objects.filter(pk=pk).first()
        remainder = reagent.remainder - new_quantity_of_consumption
        reagent.date_of_consumption = new_date_of_consumption
        reagent.quantity_of_consumption = new_quantity_of_consumption
        reagent.remainder = remainder
        reagent.save()
        logger.info(msg=f'Date_consumption: {reagent.date_of_consumption},'
                        f' quantity_of_consumption: {reagent.quantity_of_consumption}, '
                        f'remainder: {reagent.remainder}')
        self.stdout.write(f'{reagent}')