from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

app_name="api"

urlpatterns = [
    path('producto/<int:pk>/', ProductoDetailView.as_view(), name='producto-detail'),
    path('producto/', ProductoListCreateView.as_view(), name='producto'),
    path('catalogo-data/',CatalogoProductoDataView.as_view(),name="catalogo_data"),
    path('producto-data/',ProductoDataView.as_view(),name="producto_data"),
    path('movimiento-data/',MovimientosDataView.as_view(),name="movimiento_data"),
    path('movimiento/', MovimientoCreateView.as_view(), name='crear_movimiento'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', logout, name='logout'),
]
