from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class Signupform(UserCreationForm):
    name=forms.CharField(label=("fullname"))
    username=forms.EmailField(label=("Email"))

    class meta:
        model=User
        fields=('name','username','password1','password2')