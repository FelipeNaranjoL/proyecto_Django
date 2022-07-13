from django.urls import path, include
from .views import Colaborador , homeUsuario, listarUsuario, agregarUsuario, modificarUsuario, eliminarUsuario, colaboradorViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user',colaboradorViewset)

urlpatterns = [
        #http://127.0.0.1:8000/usuario/colaboradores
        path('colaboradores', homeUsuario, name = "homeUsuario"),
        path('listar/', listarUsuario, name = "listaruser"),
        path('modificarusuario/<id>/', modificarUsuario, name = "modificar_producto"),
        path('agregarusuario/', agregarUsuario, name = "agregarusuario"),
        path('eliminarusuario/<id>/', eliminarUsuario, name = "eliminarusuario"),
        path('api/',include(router.urls)),


]