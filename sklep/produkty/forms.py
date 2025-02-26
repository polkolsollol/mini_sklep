from django import forms
from .models import Produkt

class ProduktForm(forms.ModelForm):
    class Meta:
        model = Produkt
        fields = ['nazwa', 'cena']
        widgets = {
            'nazwa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwa produktu'}),
            'cena': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cena produktu'}),
        }
