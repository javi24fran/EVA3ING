# Generated by Django 3.2 on 2024-11-28 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apoderado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('run', models.CharField(max_length=12)),
                ('nacionalidad', models.CharField(max_length=50)),
                ('oficio', models.CharField(max_length=100)),
                ('domicilio', models.CharField(max_length=200)),
                ('nivel_educacional', models.CharField(choices=[('Preescolar', 'Preescolar'), ('ed_basica', 'Educación Básica'), ('ed_media', 'Educación Media'), ('ed_superior', 'Educación Superior'), ('Ninguno', 'Ninguno')], default='Ninguno', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('run', models.CharField(max_length=12)),
                ('fecha_nacimiento', models.DateField()),
                ('etnia', models.CharField(choices=[('Si', 'Sí'), ('No', 'No')], default='No', max_length=3)),
                ('numero_emergencia', models.CharField(max_length=15)),
                ('colegio_procedencia', models.CharField(max_length=200)),
                ('beneficio_junaeb', models.CharField(choices=[('Beca_baes', 'Beca de Alimentación Escolar'), ('Beca_enseñanza', 'Beca de Enseñanza Media'), ('Beca_presidente', 'Beca Presidente de la República'), ('Ninguno', 'Ninguno')], default='Ninguno', max_length=20)),
                ('sistema_salud', models.CharField(choices=[('Fonasa', 'Fonasa'), ('Isapre', 'Isapre'), ('Privado', 'Salud Privada'), ('Ninguno', 'Sin Sistema de Salud')], default='Ninguno', max_length=20)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('apoderado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alumnos', to='matriculaapp.apoderado')),
            ],
        ),
    ]
