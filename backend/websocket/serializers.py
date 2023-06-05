
from rest_framework import serializers

from .models import Temperature, Pressure

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ['id', 'timestamp', 'value']

class PressureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pressure
        fields = ['id', 'timestamp', 'value']
