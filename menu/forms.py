from django import forms
from .models import *


class PeopleOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
