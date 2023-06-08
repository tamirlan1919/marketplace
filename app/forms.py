from django import forms
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class SignupForm(UserCreationForm): 
    email = forms.EmailField(max_length=200, help_text='Required') 
    class Meta: 
        model = User 
        fields =('username', 'email', 'password1', 'password2') 
