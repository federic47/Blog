from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# ***************Model Noticia************************#
class Culture(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo= models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=150)
    autor = models.CharField(max_length=50)
    fecha = models.DateTimeField(max_length=50)
    imagen = models.ImageField(upload_to='posteo', blank=True, null=True)


    def __str__(self):
        return self.titulo +"---"+self.autor+"---"+str(self.fecha)

#******************Model deporte**********************#
class Sports(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo= models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=150)
    autor = models.CharField(max_length=50)
    fecha = models.DateTimeField(max_length=50)
    imagen = models.ImageField(upload_to='posteo', blank=True, null=True)


    def __str__(self):
        return self.titulo +"---"+self.autor+"---"+str(self.fecha)

#********************Model Economia ********************#
class Economy(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo= models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=150)
    autor = models.CharField(max_length=50)
    fecha = models.DateTimeField(max_length=50)
    imagen = models.ImageField(upload_to='posteo', blank=True, null=True)


    def __str__(self):
        return self.titulo +"---"+self.autor+"---"+str(self.fecha)

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    avatar= models.ImageField(upload_to='avatar', blank=True, null=True)


class Mensaje(models.Model):
    usuario = models.CharField(max_length=50)
    asunto = models.CharField(max_length=50)
    campo = models.CharField(max_length=50)