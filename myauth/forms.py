#path -> users/forms.py

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class MyUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label='Имя', help_text='',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}))
    last_name = forms.CharField(label='Фамилия',  help_text='',
                                widget=(forms.TextInput(attrs={'class': 'form-control','placeholder': 'Фамилия'})))
    username = forms.CharField(label='Имя пользователя',
                               help_text='',
                               error_messages = {'unique': 'Такой пользователь уже есть.'},
                               widget = forms.TextInput(attrs={'class': 'form-control','placeholder': 'Имя пользователя'})),
    password1 = forms.CharField(label='Пароль',
                                widget=(forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Пароль'})),
                                help_text=''),
    password2 = forms.CharField(label='Пароль еще раз',
                                widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Пароль еще раз'}),
                                help_text='')

    class Meta:
        model = User
        fields = ( 'first_name', 'last_name', 'username', 'password1', 'password2',)

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

#baltlogs.com