from django.db import models

class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=30)
    apellido_cliente = models.CharField(max_length=50)
    telefono_cliente = models.CharField(max_length=50, blank=True, null=True)
    email_cliente = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    direccion_cliente = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__ (self): 
            return self.nombre_cliente, self.apellido_cliente, self.telefono_cliente, self.email_cliente, self.direccion_cliente
        