from typing import Any, Dict, Tuple
from django.db import models

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen')
    descripcion = models.TextField(verbose_name='Descripción')
    autor = models.TextField(max_length=100, verbose_name='Autor')
    
    def __str__(self):
        fila = "Titulo: " + self.titulo + "-" + "Descripción: " + self.descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()