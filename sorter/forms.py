from django import forms
from .models import Sorter

class SorterForm(forms.ModelForm):
    class Meta:
        model = Sorter
        fields = [
            'unsortedList',
        ]


