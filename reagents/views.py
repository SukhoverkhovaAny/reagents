from django.shortcuts import render
from django.http import HttpResponse
from .models import Reagent, User
from .forms import UserForm, AddConsumptionForm
import logging

logger = logging.getLogger(__name__)
FORMAT = '{asctime:20} - {levelname:10} - "{name}" : {msg}'
logging.basicConfig(format=FORMAT, style='{', filename='log/django.log', filemode='a',
                    level=logging.INFO)


def main(request):
    context = {
        'title': 'Главная страница',
        'name': 'Журнал учета реактивов',
        'start_date': '10.01.2024',
        'end_date': '-',
        'responsible': 'Sukhoverkhova Anna'
    }
    return render(request, 'reagents/main.html', context)


def user_autho_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Такого пользователя не существует'
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            password = form.cleaned_data['password']
            users = User.objects.all()
            for user in users:
                if user.name == name and user.surname == surname and user.password == password:
                    message = 'Пользователь авторизирован'
                    logger.info(msg=f'User_name: {user.name}, user_surname: {user.surname}')
                    context = {
                        'title': 'Содержание',
                        'user_fullname': name + ' ' + surname
                    }
                    return render(request, 'reagents/user_content.html', context)
        else:
            message = 'Ошибка ввода данных'
    else:
        form = UserForm()
        message = 'Авторизируйтесь для заполнения расхода'
    return render(request, 'reagents/user_autho_form.html', {'form': form, 'message': message})


def content(request):
    context = {
        'title': 'Содержание',
        'list': 'Список реактивов'
    }
    return render(request, 'reagents/content.html', context)


def user_content(request):
    context = {
        'title': 'Содержание',
        'list': 'Список реактивов'
    }
    return render(request, 'reagents/user_content.html', context)


def show_petr_ether(request):
    reagents = Reagent.objects.filter(name='Петролейный эфир').all()
    context = {
        'title': 'Петролейный эфир',
        'name_reagent': 'Петролейный эфир',
        'normative_doc': 'ТУ 2631-074-44493179-01',
        'reagents': reagents
    }
    return render(request, 'reagents/show_reagent.html', context)


def user_show_petr_ether(request):
    reagents = Reagent.objects.filter(name='Петролейный эфир').all()
    context = {
        'title': 'Петролейный эфир',
        'name_reagent': 'Петролейный эфир',
        'normative_doc': 'ТУ 2631-074-44493179-01',
        'reagents': reagents
        }
    return render(request, 'reagents/user_show_reagent.html', context)


def show_chloro(request):
    reagents = Reagent.objects.filter(name='Хлороформ').all()
    context = {
        'title': 'Хлороформ',
        'name_reagent': 'Хлороформ',
        'normative_doc': 'ТУ 2631-066-44493179-01',
        'reagents': reagents
    }
    return render(request, 'reagents/show_reagent.html', context)


def user_show_chloro(request):
    reagents = Reagent.objects.filter(name='Хлороформ').all()
    context = {
        'title': 'Хлороформ',
        'name_reagent': 'Хлороформ',
        'normative_doc': 'ТУ 2631-066-44493179-01',
        'reagents': reagents
    }
    return render(request, 'reagents/user_show_reagent.html', context)


def show_silica(request):
    reagents = Reagent.objects.filter(name='Силикагель').all()
    context = {
        'title': 'Силикагель',
        'name_reagent': 'Силикагель',
        'normative_doc': 'ГОСТ 3956-76',
        'reagents': reagents
    }
    return render(request, 'reagents/show_reagent.html', context)


def user_show_silica(request):
    reagents = Reagent.objects.filter(name='Силикагель').all()
    context = {
        'title': 'Силикагель',
        'name_reagent': 'Силикагель',
        'normative_doc': 'ГОСТ 3956-76',
        'reagents': reagents
    }
    return render(request, 'reagents/user_show_reagent.html', context)


def show_naoh(request):
    reagents = Reagent.objects.filter(name='Натрия гидроокись').all()
    context = {
        'title': 'Натрия гидроокись',
        'name_reagent': 'Натрия гидроокись',
        'normative_doc': 'ГОСТ 4328-77',
        'reagents': reagents
    }
    return render(request, 'reagents/show_reagent.html', context)


def user_show_naoh(request):
    reagents = Reagent.objects.filter(name='Натрия гидроокись').all()
    context = {
        'title': 'Натрия гидроокись',
        'name_reagent': 'Натрия гидроокись',
        'normative_doc': 'ГОСТ 4328-77',
        'reagents': reagents
    }
    return render(request, 'reagents/user_show_reagent.html', context)


def add_consumption_form(request, id_reagent):
    if request.method == 'POST':
        form = AddConsumptionForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date_of_consumption']
            quantity = form.cleaned_data['quantity_of_consumption']
            reagent = Reagent.objects.filter(pk=id_reagent).first()
            reagent.date_of_consumption = date
            reagent.quantity_of_consumption = quantity
            if reagent.remainder is None:
                reagent.remainder = reagent.instance - quantity
            else:
                reagent.remainder = reagent.remainder - quantity
            reagent.save()
            logger.info(msg=f'Added consumption {reagent.name}: date: {reagent.date_of_consumption},'
                            f' quantity: {reagent.quantity_of_consumption}, remainder: {reagent.remainder}')
            context = {
                'title': 'Добавление расхода',
                'date_of_consumption': reagent.date_of_consumption,
                'quantity_of_consumption': reagent.quantity_of_consumption,
                'remainder': reagent.remainder
            }
            return render(request, 'reagents/user_content.html', context)
        else:
            message = 'Ошибка ввода данных'
    else:
        form = AddConsumptionForm()
        message = 'Введите расход'
    return render(request, 'reagents/add_consumption.html', {'form': form, 'message': message})










# Create your views here.
