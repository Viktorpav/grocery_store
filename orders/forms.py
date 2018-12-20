from django import forms
from .models import *

class CheckOutForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
