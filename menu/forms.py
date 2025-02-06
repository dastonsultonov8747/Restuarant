from django import forms
from .models import *


class PeopleOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['ismi', 'fmiliasi', 'email', 'tel', 'table', 'buyurma_sanasi', 'mehmonlar_soni', 'maxsus_sorovlar']

