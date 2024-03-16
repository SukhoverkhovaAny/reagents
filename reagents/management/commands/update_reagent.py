from django.core.management.base import BaseCommand
from reagents.models import Reagent


class Command(BaseCommand):
    help = "Update reagent by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Reagent ID')
        parser.add_argument("new_name", type=str, help="Reagent new_name")
        parser.add_argument("new_regulatory_document_of_manufacture", type=str,
                            help="New regulatory document of manufacture")
        parser.add_argument("new_receipt_date", type=str, help="Reagent new receipt date")
        parser.add_argument("new_instance", type=str, help="Reagent new_instance")
        parser.add_argument("new_qualification", type=str, help="Degree of reagent purity")
        parser.add_argument("new_shipment", type=str, help="Reagent batch")
        parser.add_argument("new_date_of_manufacture", type=str, help="Reagent new date of manufacture")
        parser.add_argument("new_best_before_date", type=str, help="Reagent new best before date")

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        new_name = kwargs.get('new_name')
        new_regulatory_document_of_manufacture = kwargs.get('new_regulatory_document_of_manufacture')
        new_receipt_date = kwargs.get('new_receipt_date')
        new_instance = kwargs.get('new_instance')
        new_qualification = kwargs.get('new_qualification')
        new_shipment = kwargs.get('new_shipment')
        new_date_of_manufacture = kwargs.get('new_date_of_manufacture')
        new_best_before_date = kwargs.get('new_best_before_date')
        reagent = Reagent.objects.filter(pk=pk).first()
        reagent.name = new_name
        reagent.regulatory_document_of_manufacture = new_regulatory_document_of_manufacture
        reagent.receipt_date = new_receipt_date
        reagent.instance = new_instance
        reagent.qualification = new_qualification
        reagent.shipment = new_shipment
        reagent.date_of_manufacture = new_date_of_manufacture
        reagent.best_before_date = new_best_before_date
        reagent.save()

        self.stdout.write(f'{reagent}')