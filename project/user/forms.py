from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    c_password = forms.CharField(widget=forms.PasswordInput)
    # p_image=forms.ImageField()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    pass1 = forms.CharField(widget=forms.PasswordInput)
