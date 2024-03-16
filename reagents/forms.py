from django import forms


class UserForm(forms.Form):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'placeholder': 'Введите имя'}))
    surname = forms.CharField(max_length=50,
                              widget=forms.TextInput(attrs={'class': 'form-control',
                                                                             'placeholder': 'Введите фамилию'}))
    password = forms.CharField(min_length=6,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                 'placeholder': 'Введите пароль'}))


class AddConsumptionForm(forms.Form):
    date_of_consumption = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control',
                                                                        'placeholder': 'Введите дату'}))
    quantity_of_consumption = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                               'placeholder': 'Введите количество'}))


