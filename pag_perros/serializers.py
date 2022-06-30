from dataclasses import field, fields
from .models import agregar
from rest_framework import serializers

class AgregarSerializer(serializers.ModelSerializer):
    class Meta:
        model = agregar
        fields = '__all__'