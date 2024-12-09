from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from api.models import Producto
from api.serializers import ProductoSerializer


# Create your views here.
class ProductoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
class ProductoListCreateView(ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    