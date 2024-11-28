from django import forms
from django.contrib.auth.forms import AuthenticationForm
from matriculaapp. models import Alumno, Apoderado
import re

class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': "Proporcione un nombre de usuario y una contraseña válida.",
    }
from django.core.exceptions import ValidationError

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'run','fecha_nacimiento', 'etnia', 'numero_emergencia', 'colegio_procedencia', 'beneficio_junaeb', 'sistema_salud']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Ingrese Fecha Nacimiento'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Apellido'}),
            'run': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese RUN'}),
            'numero_emergencia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese número de emergencia'}),
            'colegio_procedencia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre Colegio de Procedencia'}),
            'etnia': forms.Select(attrs={'class': 'form-control'}),
            'beneficio_junaeb': forms.Select(attrs={'class': 'form-control'}),
            'sistema_salud': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_numero_emergencia(self):
        numero_emergencia = self.cleaned_data.get('numero_emergencia')
        if not numero_emergencia.isdigit():
            raise forms.ValidationError('El número de emergencia debe contener solo números.')
        if len(numero_emergencia) < 9:
            raise forms.ValidationError('El número de emergencia debe tener al menos 9 dígitos.')
        return numero_emergencia

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres.')
        if any(char.isdigit() for char in nombre):
            raise forms.ValidationError('El nombre no puede contener números.')
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido')
        if len(apellido) < 3:
            raise forms.ValidationError('El apellido debe tener al menos 3 caracteres.')
        if any(char.isdigit() for char in apellido):
            raise forms.ValidationError('El apellido no puede contener números.')
        return apellido
    
    def clean_run(self):
        run = self.cleaned_data.get('run')
        
        run_pattern = r'^\d{7,8}-[0-9kK]$'
        
        if not re.match(run_pattern, run):
            raise forms.ValidationError('El RUN debe tener el formato: 12345678-9')

        numero, digito = run.split('-')

        if not numero.isdigit() or len(numero) < 7 or len(numero) > 8:
            raise forms.ValidationError('El número del RUN debe tener entre 7 y 8 dígitos.')

        if not (digito.isdigit() or digito.lower() == 'k'):
            raise forms.ValidationError('El dígito verificador debe ser un número o la letra "K".')
        
        return run

    
class ApoderadoForm(forms.ModelForm):
    class Meta:
        model = Apoderado
        fields = ['nombre', 'apellido', 'run', 'nacionalidad', 'oficio', 'domicilio', 'nivel_educacional']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Apellido'}),
            'run': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese RUN'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nacionalidad'}),
            'oficio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese trabajo u oficio'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese domicilio'}),
            'nivel_educacional': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_run(self):
        run = self.cleaned_data.get('run')
        
        run_pattern = r'^\d{7,8}-[0-9kK]$'
        
        if not re.match(run_pattern, run):
            raise forms.ValidationError('El RUN debe tener el formato: 12345678-9')

        numero, digito = run.split('-')

        if not numero.isdigit() or len(numero) < 7 or len(numero) > 8:
            raise forms.ValidationError('El número del RUN debe tener entre 7 y 8 dígitos.')

        if not (digito.isdigit() or digito.lower() == 'k'):
            raise forms.ValidationError('El dígito verificador debe ser un número o la letra "K".')
        
        return run

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres.')
        if any(char.isdigit() for char in nombre):
            raise forms.ValidationError('El nombre no puede contener números.')
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido')
        if len(apellido) < 3:
            raise forms.ValidationError('El apellido debe tener al menos 3 caracteres.')
        if any(char.isdigit() for char in apellido):
            raise forms.ValidationError('El apellido no puede contener números.')
        return apellido