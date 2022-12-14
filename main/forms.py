from .models import Cafe
from django.forms import ModelForm, TextInput, Textarea, NumberInput

class CafeForm(ModelForm):
    class Meta:
        model = Cafe
        fields = ['title', 'address', 'text', 'price', 'published']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ввіедіть назву закладу'
            }),
            'address': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ввіедіть адресу закладу'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ввіедіть короткий опис закладу'
            }),
            'price': NumberInput(attrs={
                'class': 'col-xs-2',
                'id': 'ex2',
                'placeholder': 'Ввіедіть середній чек'
            }),
        }
