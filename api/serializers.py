from rest_framework import serializers
from .models import Producto, Movimimientos, StockProductos
from .models import tipo_movimiento

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

    def validate_cantidad(self, value):
        if value <= 0:
            raise serializers.ValidationError("La cantidad no puede ser negativa ni 0.")
        return value
    def validate_costo_unitario(self, value):
        if value <= 0:
            raise serializers.ValidationError("El costo unitario no puede ser negativo ni 0.")
        return value
    def validate_precio_venta(self, value):
        if value <= 0:
            raise serializers.ValidationError("El precio de venta no puede ser negativo ni 0. ")
        return value
class MovimientoSerializer(serializers.ModelSerializer):
    tipo = serializers.ChoiceField(choices=tipo_movimiento)
    producto = serializers.PrimaryKeyRelatedField(queryset=StockProductos.objects.all())
    
    class Meta:
        model = Movimimientos
        fields = ['cantidad', 'tipo', 'producto', 'comentario']
    
    def create(self, validated_data):
        tipo_movimiento = validated_data['tipo']
        cantidad = validated_data['cantidad']
        producto = validated_data['producto']
        movimiento = Movimimientos.objects.create(**validated_data)
        stock_producto = producto
        if tipo_movimiento == 1: 
            stock_producto.cantidad_disponible += cantidad
        elif tipo_movimiento == 2: 
            stock_producto.cantidad_disponible -= cantidad
        
        stock_producto.save()
        
        return movimiento