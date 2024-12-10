from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from productos_app.forms import AddStockProductoForm, ProductoModelForm
# Create your views here.

class IndexView(TemplateView):
    template_name="index.html"
    form_class = AddStockProductoForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"]=self.form_class()
        return context
class ListCatalogoProductos(TemplateView):
    template_name="list_catalogo_productos.html"
    form_class = ProductoModelForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"]=self.form_class()
        return context
class ListMovimientos(TemplateView):
    template_name="list_movimientos.html"
class LoginView(TemplateView):
    template_name="user_login.html"

