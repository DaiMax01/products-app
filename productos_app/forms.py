from django import forms

from api.models import Producto, StockProductos
from api.models import tipo_movimiento

class ProductoModelForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields='__all__'
        
class AddStockProductoForm(forms.Form):
    cantidad = forms.IntegerField(min_value=1)
    tipo = forms.ChoiceField(choices=tipo_movimiento)
    producto = forms.ModelChoiceField(queryset=StockProductos.objects.all())
    comentario = forms.CharField()
    
