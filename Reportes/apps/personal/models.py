from django.db import models
# Create your models here.

class Unidad(models.Model):
    nombre = models.CharField(max_length=50 )

    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    unidad = models.ForeignKey(Unidad, on_delete='CASCADE')

    def __str__(self):
        return self.nombre

class Personal(models.Model):
    nombre = models.CharField(max_length=50)
    ape_pat = models.CharField(max_length=50)
    ape_mat = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=False)
    password = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    extension = models.IntegerField(null=True, blank=True)
    departamento = models.ForeignKey(Departamento, on_delete=None)
    unidad = models.ForeignKey(Unidad, on_delete=None)

    def __str__(self):
        return ("%s %s %s - %s" % (self.nombre, self.ape_pat, self.ape_mat, self.departamento))
