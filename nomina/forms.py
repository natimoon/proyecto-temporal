# employees/forms.py
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['cedula', 'nombre', 'fecha_ingreso', 'cargo', 'salario']
        widgets = {
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_cedula(self):
        cedula = self.cleaned_data.get('cedula')
        if Employee.objects.filter(cedula=cedula).exists():
            raise forms.ValidationError("La cédula ya está registrada")
        return cedula
