from django.db import models




class Actores(models.Model):
    nombres = models.CharField(max_length=60, null=False, blank=False, verbose_name='Nombres')
    apellidos = models.CharField(max_length=60, null=False, blank=False, verbose_name='Apellidos')
    pais = models.CharField(max_length=50, null=False, blank=False, verbose_name='País')
    ciudad = models.CharField(max_length=50, null=False, blank=False, verbose_name='Ciudad')
    fecha_nacimiento = models.DateField(null=True, blank=True, verbose_name='Fecha de nacimiento')



class Peliculas(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Imagen')
    imagen_url = models.URLField(null=True, blank=True, verbose_name='Imagen')
    video = models.URLField(null=False, blank=False)
    descripcion_corta = models.Charfield(max_length=300, null=False, blank=False, verbose_name="descripción corta")
    descripcion = models.TextField(null=False, blank=False, verbose_name='descripción')