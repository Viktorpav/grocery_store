from django.db import models



'''
from django.core.exceptions import ValidationError
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.core.validators import validate_email

class Registration_form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),max_length=50, required=True, unique=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),max_length=50, required=True, unique=True)
    email_reg = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),max_length=50, required=True, unique=True)
    password_reg = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),max_length=50, required=True)
    confirm_password_reg = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}),max_length=50, required=True)

    class Meta():
        model = Registration_form
        fields = ['name', 'username', 'email_reg', 'password_reg', 'confirm_password_reg']

class Login_form(forms.ModelForm):
    email_log = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),max_length=50, required=True)
    password_log = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),max_length=50, required=True)

    class Meta():
        model = Login_form
        fields = ['email_log', 'password_log']

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            match = Username.objects.get(name = username)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError('Username already exist')

        def clean_email(self):
            email = self.cleaned_data['username']
            try:
                match = Username.objects.get(name = username)
            except:
                return self.cleaned_data['username']
            raise forms.ValidationError('Username already exist')
'''