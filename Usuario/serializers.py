from dataclasses import field, fields
from .models import Colaborador
from rest_framework import serializers

class colaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaborador
        fields = '__all__'