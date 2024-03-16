from django.core.management.base import BaseCommand
from reagents.models import Reagent


class Command(BaseCommand):
    help = "Create Reagent"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="Reagent Name")
        parser.add_argument("regulatory_document_of_manufacture", type=str, help="Regulatory document of manufacture")
        parser.add_argument("receipt_date", type=str, help="Reagent receipt date")
        parser.add_argument("instance", type=float, help="Reagent instance")
        parser.add_argument("qualification", type=str, help="Qualification of reagent")
        parser.add_argument("shipment", type=str, help="Reagent batch")
        parser.add_argument("date_of_manufacture", type=str, help="Reagent date of manufacture")
        parser.add_argument("best_before_date", type=str, help="Reagent best before date")

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        regulatory_document_of_manufacture = kwargs.get('regulatory_document_of_manufacture')
        receipt_date = kwargs.get('receipt_date')
        instance = kwargs.get('instance')
        qualification = kwargs.get('qualification')
        shipment = kwargs.get('shipment')
        date_of_manufacture = kwargs.get('date_of_manufacture')
        best_before_date = kwargs.get('best_before_date')

        reagent = Reagent(name=name, regulatory_document_of_manufacture=regulatory_document_of_manufacture,
                          receipt_date=receipt_date, instance=instance, qualification=qualification,
                          shipment=shipment, date_of_manufacture=date_of_manufacture,
                          best_before_date=best_before_date)
        reagent.save()
        self.stdout.write(f'{reagent}')