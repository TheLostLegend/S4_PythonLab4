from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task
from django.forms import ModelForm, TextInput, Textarea
from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "text"]
        widgets = {
            "title": TextInput(attrs={
                "placeholder": "Введите название",
                "class": "form-control",
            }),
            "text": Textarea(attrs={
                "placeholder": "Введите описание",
                "class": "form-control",
            }),
        }


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {'password': forms.PasswordInput()}