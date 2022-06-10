from django import forms
from .models import Producent, Produkty

class Produktform(forms.ModelForm):
    class Meta:
        model = Produkty
        fields = [
            'nazwa',
            'opis',
            'cena'
            ]