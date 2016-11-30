from django.conf.urls import url 
from .views import RegistroUsuario, Bienvenido

urlpatterns = [
	url(r'^registrar', RegistroUsuario.as_view(), name="registrar"),
	url(r'^bienvenido', Bienvenido, name="bienvenido"),
]