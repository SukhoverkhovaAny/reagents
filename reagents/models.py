from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=45)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'Username: {self.name}, Surname: {self.surname}'


class Reagent(models.Model):
    name = models.CharField(max_length=100)
    regulatory_document_of_manufacture = models.CharField(max_length=100) # НД изготовления
    receipt_date = models.DateField() # дата поступления
    instance = models.FloatField() # количество
    qualification = models.CharField(max_length=50) # степень чистоты
    shipment = models.CharField(max_length=10)# партия
    date_of_manufacture = models.DateField() # дата изготовления
    best_before_date = models.DateField() # срок годности
    date_of_consumption = models.DateField(blank=True, null=True) # дата расхода
    quantity_of_consumption = models.FloatField(blank=True, null=True) # количество расхода
    remainder = models.FloatField(blank=True, null=True) # остаток

    def __str__(self):
        return f'Reagent_name: {self.name}, quantity_upon_receipt: {self.instance},  shipment: {self.shipment},' \
               f' date_of_manufacture: {self.date_of_manufacture}, expiration_date: {self.best_before_date}, ' \
               f'remainder: {self.remainder}'






