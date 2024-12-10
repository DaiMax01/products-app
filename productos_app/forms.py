from django import forms

from api.models import Producto, StockProductos
from api.models import tipo_movimiento

class ProductoModelForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields='__all__'
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad < 0:
            raise forms.ValidationError("La cantidad no puede ser negativa.")
        return cantidad
    def clean_costo_unitario(self):
        costo_unitario = self.cleaned_data.get('costo_unitario')
        if costo_unitario < 0:
            raise forms.ValidationError("El precio de venta no puede ser negativo.")
        return costo_unitario
    def clean_precio_venta(self):
        precio_venta = self.cleaned_data.get('precio_venta')
        if precio_venta < 0:
            raise forms.ValidationError("El precio de venta no puede ser negativo.")
        return precio_venta
class AddStockProductoForm(forms.Form):
    cantidad = forms.IntegerField(min_value=1)
    tipo = forms.ChoiceField(choices=tipo_movimiento)
    producto = forms.ModelChoiceField(queryset=StockProductos.objects.all())
    comentario = forms.CharField(required=False)
    
