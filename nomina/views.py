from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Empleado, Cargo, Usuario, HistorialLaboral
from .serializers import EmpleadoSerializer, CargoSerializer, UsuarioSerializer, HistorialLaboralSerializer

class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    permission_classes = [IsAuthenticated]

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class HistorialLaboralViewSet(viewsets.ModelViewSet):
    queryset = HistorialLaboral.objects.all()
    serializer_class = HistorialLaboralSerializer
    permission_classes = [IsAuthenticated]