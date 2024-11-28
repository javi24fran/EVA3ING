from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    run = models.CharField(max_length=12)
    fecha_nacimiento = models.DateField()
    

    ETNIA_CHOICES = [
        ('Si', 'Sí'),
        ('No', 'No'),
    ]
    etnia = models.CharField(
        max_length=3,
        choices=ETNIA_CHOICES,
        default='No'
    )
    

    numero_emergencia = models.CharField(max_length=15)
    

    colegio_procedencia = models.CharField(max_length=200)
    

    BENEFICIOS_CHOICES = [
        ('Beca_baes', 'Beca de Alimentación Escolar'),
        ('Beca_enseñanza', 'Beca de Enseñanza Media'),
        ('Beca_presidente', 'Beca Presidente de la República'),
        ('Ninguno', 'Ninguno'),
    ]
    beneficio_junaeb = models.CharField(
        max_length=20, 
        choices=BENEFICIOS_CHOICES, 
        default='Ninguno'
    )
    

    SISTEMA_SALUD_CHOICES = [
        ('Fonasa', 'Fonasa'),
        ('Isapre', 'Isapre'),
        ('Privado', 'Salud Privada'),
        ('Ninguno', 'Sin Sistema de Salud'),
    ]
    sistema_salud = models.CharField(
        max_length=20,
        choices=SISTEMA_SALUD_CHOICES,
        default='Ninguno'
    )
    

    fecha_registro = models.DateTimeField(auto_now_add=True)
    apoderado = models.ForeignKey(
        'Apoderado', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='alumnos')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Apoderado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    run = models.CharField(max_length=12)
    nacionalidad = models.CharField(max_length=50)
    oficio = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=200)

    NIVEL_CHOICES = [
    ('Preescolar', 'Preescolar'),
    ('ed_basica', 'Educación Básica'),
    ('ed_media', 'Educación Media'),
    ('ed_superior', 'Educación Superior'),
    ('Ninguno', 'Ninguno'),
    ]
    nivel_educacional = models.CharField(
        max_length=20, 
        choices=NIVEL_CHOICES, 
        default='Ninguno')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
