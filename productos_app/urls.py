from django.urls import include, path
from .views import * 

app_name="productos"

urlpatterns = [
    path('', IndexView.as_view(), name='index_view'),
    path('login', LoginView.as_view(), name='login_view'),
]
