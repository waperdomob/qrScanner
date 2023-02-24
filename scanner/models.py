from random import choices
from django.db import models
from django.forms import model_to_dict
from django.conf import settings

# Create your models here.

class Cursos(models.Model):
    nombre_curso = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=45)
    def __str__(self):
        return self.nombre_curso

    def toJSON(self):
        item = model_to_dict(self)
        item['nombre_curso'] = self.nombre_curso
        return item

class Inscrito(models.Model):
    Nombres = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, unique=True)
    celular = models.CharField(max_length=100, unique=True)
    ciudad = models.CharField(max_length=45,null=True, blank=True)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombres

    def toJSON(self):
        item = model_to_dict(self)   
        item['full_name'] = self.Nombres
        return item

class Industria(models.Model):
    industria = models.CharField(max_length=100, null=False)
    ciudad = models.CharField(max_length=45,null=True, blank=True)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)

    def __str__(self):
        return self.industria

class Ingreso(models.Model):
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    Nombres = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, unique=True)
    celular = models.CharField(max_length=100, unique=True)
    ciudad = models.CharField(max_length=45,null=True, blank=True)
    industria = models.ForeignKey(Industria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Nombres