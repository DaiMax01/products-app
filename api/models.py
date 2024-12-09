from django.db import models


tipo_movimiento =((1,"ENTRADA"),(2,"SALIDA"))

class Producto(models.Model):
    descripcion = models.CharField(max_length=100)
    costo_unitario = models.DecimalField(decimal_places=4, max_digits=14, null=True)
    precio_venta = models.DecimalField(decimal_places=4, max_digits=14, null=True)
    

class StockProductos(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="stocks")
    cantidad_disponible = models.BigIntegerField(default=0)
    valor_total = models.DecimalField(decimal_places=4, max_digits=14)
    
    def __str__(self):
        return f"{self.producto.descripcion}"




class Movimimientos():
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="movimientos")
    tipo = models.IntegerField(choices=tipo_movimiento)
    cantidad = models.BigIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField(null=True, blank=True)
    