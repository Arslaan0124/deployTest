from django import forms
from .models import SortArray

class SorterForm(forms.ModelForm):
    class Meta:
        model = SortArray
        fields = [
            'unsortedList',
        ]
    