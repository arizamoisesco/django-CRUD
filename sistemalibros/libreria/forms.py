from dataclasses import field
from django import forms
from .models import Libro

class LibrosForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'