from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('producto/<int:pk>/', ProductoDetailView.as_view(), name='producto-detail'),
    path('producto/', ProductoListCreateView.as_view(), name='producto-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
