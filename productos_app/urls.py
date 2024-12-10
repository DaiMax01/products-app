from django.urls import include, path
from .views import * 

app_name="productos"

urlpatterns = [
    path('', IndexView.as_view(), name='index_view'),
    path('catalogo', ListCatalogoProductos.as_view(), name='catalogo_view'),
    path('movimientos',ListMovimientos.as_view(),name="movimientos_view"),
    path('login', LoginView.as_view(), name='login_view'),
]
