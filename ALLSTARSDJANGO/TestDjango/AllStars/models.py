from django.db import models

#Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la categoria')

    def __str__(self):
        return self.nombreCategoria


class Contacto(models.Model):
    gmail = models.CharField(max_length=30, primary_key=True, verbose_name='gmail')
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    apellido = models.CharField(max_length=20, verbose_name='Apellido')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    numero = models.CharField(max_length=20, verbose_name='Numero')
    comentario = models.CharField(max_length=500, verbose_name='Comentario')

    def __str__(self):
        return self.gmail