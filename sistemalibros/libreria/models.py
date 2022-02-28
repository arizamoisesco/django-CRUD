from distutils.command.upload import upload
from turtle import title
from django.db import models

# Create your models here.
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='Titulo')
    image = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    description = models.TextField(verbose_name='Descripción', null=True)

    def __str__(self):
        fila = f"Titulo: {self.title} - Descripción {self.description}"
        return fila

#Borra la imágen almacenada del sistema directamente
    def delete(self, using = None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()