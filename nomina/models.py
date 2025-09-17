from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo de Usuario para manejar roles
class Usuario(AbstractUser):
    ROL_CHOICES = (
        ('admin', 'Administrador'),
        ('gerente', 'Gerente'),
        ('empleado', 'Empleado'),
    )
    rol = models.CharField(max_length=10, choices=ROL_CHOICES, default='empleado')

# Modelo para los cargos de la empresa
class Cargo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

# Modelo para la información principal del empleado
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    vinculos = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    salario_actual = models.DecimalField(max_digits=10, decimal_places=2)
    cargo_actual = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True)

# Modelo para el historial de cargos y salarios del empleado
class HistorialLaboral(models.Model):
    empleado = models.OneToOneField(Empleado, on_delete=models.CASCADE, related_name='historial')
    historial = models.JSONField(default=list)