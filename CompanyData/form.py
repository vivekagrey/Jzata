
from django import forms 


class Login(forms.Form):
    username = forms.CharField(max_length=100)
    password  = forms.CharField(widget=forms.Textarea)




