from django.db import models

class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=30, blank=False, null=False)
    apellido_cliente = models.CharField(max_length=50, blank=False, null=False)
    telefono_cliente = models.CharField(max_length=50, blank=False, null=False)
    email_cliente = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    direccion_cliente = models.CharField(max_length=255, blank=False, null=False)
    
    def __str__ (self): 
            return self.nombre_cliente, self.apellido_cliente, self.telefono_cliente, self.email_cliente, self.direccion_cliente
        
class Proveedor(models.Model): 
    nombre_proveedor = models.CharField(max_length=30, blank=False, null=False)
    apellido_proveedor = models.CharField(max_length=50, blank=False, null=False)
    empresa_proveedor = models.CharField(max_length=50, blank=False, null=False)
    telefono_proveedor = models.CharField(max_length=50, blank=False, null=False)
    email_empresa_proveedor = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    
    def __str__ (self): 
            return self.nombre_proveedor, self.apellido_proveedor, self.empresa_proveedor, self.telefono_proveedor, self.email_empresa_proveedor

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50, blank=False, null=False)
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_producto_stock = models.IntegerField()
    proveedor_producto = models.ForeignKey(Proveedor,on_delete=models.CASCADE, blank=False, null=False)
    
    def __str__ (self): 
            return self.nombre_producto, self.precio_producto, self.cantidad_producto_stock, self.proveedor_producto

class Empleado(models.Model):
    nombre_empleado = models.CharField(max_length=30, blank=False, null=False)
    apellido_empleado = models.CharField(max_length=50, blank=False, null=False)
    cargo_empleado = models.CharField(max_length=50, blank=False, null=False)
    email_empleado = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    
    def __str__ (self): 
            return self.nombre_empleado, self.apellido_empleado, self.cargo_empleado, self.email_empleado

class MetodoPago(models.Model):
    tipo_metodo_pago = models.CharField(max_length=30, blank=False, null=False)

    def __str__ (self): 
            return self.tipo_metodo_pago
        
class Pedido(models.Model):
    nombre_producto = models.ForeignKey(Producto,on_delete=models.CASCADE, blank=False, null=False)
    tipo_metodo_pago = models.ForeignKey(MetodoPago,on_delete=models.CASCADE, blank=False, null=False)
    fecha_pedido = models.DateField(auto_now_add=True, blank=False, null=False)
    cantidad_producto_pedido = models.IntegerField()
    cliente_pedido = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=False, null=False)
    empleado_pedido = models.ForeignKey(Empleado, on_delete=models.CASCADE, blank=False, null=False)
    
    def __str__ (self): 
            return self.nombre_producto, self.tipo_metodo_pago, self.fecha_pedido, self.cantidad_producto_pedido, self.cliente_pedido, self.empleado_pedido
        
class PedidoProducto(models.Model):
    nombre_producto = models.ForeignKey(Producto,on_delete=models.CASCADE, blank=False, null=False)
    pedido_producto = models.ForeignKey(Pedido,on_delete=models.CASCADE, blank=False, null=False)

    
    def __str__ (self): 
            return self.nombre_producto, self.pedido_producto         