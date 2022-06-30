from dataclasses import field, fields
from pyexpat import model
from django import forms
from .models import agregar
from django.contrib.auth.forms import UserCreationForm


class agregarForms(forms.ModelForm):
    class Meta:
        model = agregar
        fields = ["nombre","marca","precio","peso","imagen"]
        

class CustomUserCreationForm(UserCreationForm):
    pass