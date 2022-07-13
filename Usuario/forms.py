from dataclasses import field, fields
from pyexpat import model
from django import forms
from .models import Colaborador
from django.contrib.auth.forms import UserCreationForm


class agregarColaborador(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = "__all__"
        