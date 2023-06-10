from django import forms
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class SignupForm(UserCreationForm): 
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=200, help_text='Required',widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta: 
        model = User 
        fields =('username', 'email', 'password1', 'password2') 


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name','second_name','last_name', 'date_br', 'gender', 'phone_number',
                  'address_city', 'address_street', 'address_house', 'address_podezd',
                  'address_kv', 'comment', 'notification_settings', 'user_picture')