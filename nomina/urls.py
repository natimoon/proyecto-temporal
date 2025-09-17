from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CargoViewSet, EmpleadoViewSet, UsuarioViewSet, HistorialLaboralViewSet

router = DefaultRouter()
router.register('cargos', CargoViewSet)
router.register('empleados', EmpleadoViewSet)
router.register('usuarios', UsuarioViewSet)
router.register('historial_laboral', HistorialLaboralViewSet)

urlpatterns = [
    # Puedes añadir rutas manuales aquí si lo necesitas
    # Pero las del router se agregan automáticamente con la siguiente línea
    path('', include(router.urls)),
]