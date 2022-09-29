from django.db import models

# Create your models here.

#PROVEEDORES
class Proveedor(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    rrss = models.CharField(max_length=100)
    nota = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

# SUPPORT

OPTION = (
    ('Me paso a mi','Me paso a mi'),
    ('Ya era asi','Ya era asi'),
)

REASON = (
    ('Borrar proveedor','Borrar proveedor'),
    ('Problema del sistema','Problema del sistema'),
    ('Otros','Otros'),
    
)

SITUATION = (
    ('Done','Done'),
    ('Pending','Pending'),
)

class Call(models.Model):
    terms = models.BooleanField("Tienes esta responsabilidad")
    user = models.CharField(max_length=100)
    message = models.TextField()
    option = models.CharField(max_length=100, choices=OPTION)
    reason = models.CharField(max_length=100, choices=REASON)
    created_at = models.DateTimeField(auto_now_add=True)
    Situation = models.CharField(max_length=100, null=True, choices=SITUATION, default='Pending')
    

    def __str__(self):
        return self.user