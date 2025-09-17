from rest_framework import serializers
from .models import Empleado, Cargo, Usuario, HistorialLaboral

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class HistorialLaboralSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialLaboral
        fields = '__all__'