"""ing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from matriculaapp.views import index, CustomLoginView, matricula_view,lista_alumnos,detalle_alumno,actualizar_alumno,actualizar_apoderado,eliminar_alumno
from django.contrib.auth import views as auth_views

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', index, name='index'),
    path('matricula/', matricula_view, name='matricula'),
    path('lista-alumnos/', lista_alumnos, name='lista_alumnos'),
     path('alumnos/<int:alumno_id>/', detalle_alumno, name='detalle_alumno'),
    path('alumnos/<int:alumno_id>/eliminar/', eliminar_alumno, name='eliminar_alumno'),
    path('alumnos/<int:alumno_id>/actualizar/', actualizar_alumno, name='actualizar_alumno'),
    path('alumnos/<int:alumno_id>/apoderado/', actualizar_apoderado, name='actualizar_apoderado'),

]