from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from api.models import Movimimientos, Producto, StockProductos
from api.serializers import MovimientoSerializer, ProductoSerializer
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.views.decorators.http import require_http_methods

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
# Create your views here.
class ProductoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]
    
class ProductoListCreateView(ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        producto = serializer.save()
        stock_producto = StockProductos(producto=producto,cantidad_disponible = 0, valor_total=0)
        stock_producto.save()
@method_decorator(csrf_exempt, name='dispatch')
class ProductoDataView(BaseDatatableView):
    model = StockProductos
    columns = ['id', 'nombre_producto', 'precio_unitario', 'cantidad_disponible', 'valor_total']
    def post(self, request, *args, **kwargs):

        return super().get(request, *args, **kwargs)
    
    def dispatch(self, request, *args, **kwargs):
        jwt_auth = JWTAuthentication()
        try:
            user, token = jwt_auth.authenticate(request)
            if not user:
                raise AuthenticationFailed("Usuario no autenticado")
            request.user = user
        except AuthenticationFailed as e:
            return JsonResponse({'detail': str(e)}, status=401)
        except Exception as e:
            return JsonResponse({'detail': str(e)}, status=401)
        return super().dispatch(request, *args, **kwargs)
    def filter_queryset(self, qs):
        filters = {
            'search[value]': [
                'producto__descripcion__icontains'
            ],
        }

        for param, field in filters.items():
            value = self.request.POST.get(param, None)
            if value:
                if isinstance(field, str):
                    qs = qs.filter(**{field: value})
                elif isinstance(field, list):
                    q_objects = Q()
                    for sub_field in field:
                        q_objects |= Q(**{sub_field: value})
                    qs = qs.filter(q_objects)
        
        return qs
@method_decorator(csrf_exempt, name='dispatch')
class CatalogoProductoDataView(BaseDatatableView):
    model = Producto
    columns = ['id', 'descripcion', 'costo_unitario', 'precio_venta']
    def dispatch(self, request, *args, **kwargs):
        jwt_auth = JWTAuthentication()
        try:
            user, token = jwt_auth.authenticate(request)
            if not user:
                raise AuthenticationFailed("Usuario no autenticado")
            request.user = user
        except AuthenticationFailed as e:
            return JsonResponse({'detail': str(e)}, status=401)
        except Exception as e:
            return JsonResponse({'detail': str(e)}, status=401)
        return super().dispatch(request, *args, **kwargs)
    def filter_queryset(self, qs):
        filters = {
            'search[value]': [
                'descripcion__icontains'
            ],
        }

        for param, field in filters.items():
            value = self.request.POST.get(param, None)
            if value:
                if isinstance(field, str):
                    qs = qs.filter(**{field: value})
                elif isinstance(field, list):
                    q_objects = Q()
                    for sub_field in field:
                        q_objects |= Q(**{sub_field: value})
                    qs = qs.filter(q_objects)
        
        return qs
    def post(self, request, *args, **kwargs):

        return super().get(request, *args, **kwargs)
    
@method_decorator(csrf_exempt, name='dispatch')
class MovimientosDataView(BaseDatatableView):
    model = Movimimientos
    columns = ['id','fecha_formateada', 'nombre_producto', 'tipo', 'cantidad']
    def dispatch(self, request, *args, **kwargs):
        jwt_auth = JWTAuthentication()
        try:
            user, token = jwt_auth.authenticate(request)
            if not user:
                raise AuthenticationFailed("Usuario no autenticado")
            request.user = user
        except AuthenticationFailed as e:
            return JsonResponse({'detail': str(e)}, status=401)
        except Exception as e:
            return JsonResponse({'detail': str(e)}, status=401)
        return super().dispatch(request, *args, **kwargs)
    def filter_queryset(self, qs):
        filters = {
            'search[value]': [
                'producto__producto__descripcion__icontains'
            ],
        }

        for param, field in filters.items():
            value = self.request.POST.get(param, None)
            if value:
                if isinstance(field, str):
                    qs = qs.filter(**{field: value})
                elif isinstance(field, list):
                    q_objects = Q()
                    for sub_field in field:
                        q_objects |= Q(**{sub_field: value})
                    qs = qs.filter(q_objects)
        
        return qs
    def post(self, request, *args, **kwargs):

        return super().get(request, *args, **kwargs)
class CustomTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            access_token = response.data.get('access')
            request.session['jwt_token'] = access_token

        return response
    
@require_http_methods(["GET"])
def logout(request):
    if 'jwt_token' in request.session:
        del request.session['jwt_token'] 
    return JsonResponse({"message": "Sesión cerrada exitosamente"}, status=200)


class MovimientoCreateView(CreateAPIView):
    queryset = Movimimientos.objects.all()
    serializer_class = MovimientoSerializer

    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return response