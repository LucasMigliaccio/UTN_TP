from django.forms import ModelForm
from django import forms
from .models import Producto


class SearchBebidaForm(forms.Form):
    querycom =forms.CharField(label="Ingresa el nombre de la bebida", 
                              widget=forms.TextInput(attrs={"size":32 , "class": "form- control"}))