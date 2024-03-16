from django.core.management.base import BaseCommand
from reagents.models import User


class Command(BaseCommand):
    help = "Update user by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('new_name', type=str, help='User new_name')
        parser.add_argument('new_surname', type=str, help='User new_surname')
        parser.add_argument('new_password', type=str, help='User new_password')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        new_name = kwargs.get('new_name')
        new_surname = kwargs.get('new_surname')
        new_password = kwargs.get('new_password')
        user = User.objects.filter(pk=pk).first()
        user.name = new_name
        user.surname = new_surname
        user.password = new_password
        user.save()
        self.stdout.write(f'{user}')