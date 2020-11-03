from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

#phone_regex = RegexValidator(regex=r'/^(\+\d{1,3}[- ]?)?\d{10}$/', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
class Signupform(UserCreationForm):
    name=forms.CharField(label=("fullname"))
    username=forms.EmailField(label=("Email"))
    phoneno=forms.RegexField(regex=r'^\+?1?\d{9,12}$')

    class meta:
        model=User
        fields=('name','username','password1','password2','phoneno')