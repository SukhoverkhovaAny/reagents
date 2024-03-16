from django.core.management.base import BaseCommand
from reagents.models import User


class Command(BaseCommand):
    help = "Create User"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="User Name")
        parser.add_argument("surname", type=str, help="User Surname")
        parser.add_argument("password", type=str, help="User password")

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        surname = kwargs.get('surname')
        password = kwargs.get('password')

        user = User(name=name, surname=surname, password=password)
        user.save()

        self.stdout.write(f'{user}')
