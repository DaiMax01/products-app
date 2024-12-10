import jwt
import re
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.authentication import JWTAuthentication

from konverzaprueba import settings

class JWTTokenMiddleware(MiddlewareMixin):
    def process_request(self, request):
        token = request.session.get('jwt_token', None)
        current_path = request.path
        if not (re.match(r'^/login',current_path) or re.match(r'^/api/token',current_path)):
            try:
                decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                request.user_data = decoded_token
            except Exception as e:
                if token:
                    del request.session['jwt_token']
                return HttpResponseRedirect(reverse('productos:login_view'))
            