from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        fields = ('username', 'password1', 'password2')
        model = get_user_model()
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите логин',
                                      'class': 'form-input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль',
                                                             'class': 'form-input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтверждение пароля',
                                                                  'class': 'form-input'}))