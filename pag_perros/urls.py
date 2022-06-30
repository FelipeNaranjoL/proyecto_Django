from django.urls import path, include
# vas a importar cada funcion de la carpeta views.py
from .views import home, alimentos, formulario, no_producto, pelis,\
    listar, agregarform, modificar_producto, eliminar, registro, AgregarViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto',AgregarViewset)

#aqui creas las direcciones urls para que la persona pueda llegar a la pagina que desees
urlpatterns = [
    path('', home, name = "home"),
    path('alimentos/', alimentos, name = "alimentos"),
    path('formulario/', formulario, name = "formulario"),
    path('no_producto/', no_producto, name = "no_producto"),
    path('pelis/', pelis, name = "pelis"),
    path('listar/', listar, name = "listar"),
    path('agregar_producto/', agregarform, name = "agregar_producto"),
    path('modificar_producto/<id>/', modificar_producto, name = "modificar_producto"),
    path('eliminar_producto/<id>/', eliminar, name = "eliminar_producto"),
    path('registro/', registro, name = "registro"),
    path('api/',include(router.urls)),
]