from django.db import models

# ***************Model Noticia************************#
class Culture(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo= models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=150)
    autor = models.CharField(max_length=50)
    fecha = models.DateTimeField(max_length=50)
    #imagen = models.ImageField()


    def __str__(self):
        return self.titulo +"---"+self.autor+"---"+str(self.fecha)

#******************Model deporte**********************#
class Sports(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo= models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=150)
    autor = models.CharField(max_length=50)
    fecha = models.DateTimeField(max_length=50)
    #imagen = models.ImageField()


    def __str__(self):
        return self.titulo +"---"+self.autor+"---"+str(self.fecha)

#********************Model Economia ********************#
class Economy(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo= models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=150)
    autor = models.CharField(max_length=50)
    fecha = models.DateTimeField(max_length=50)
    #imagen = models.ImageField()


    def __str__(self):
        return self.titulo +"---"+self.autor+"---"+str(self.fecha)