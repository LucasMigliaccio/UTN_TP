from django.urls import path
from .views import EjemploTienda, VerImagenes, ver_imagen, para_ajax, BuscarBebida, BuscarBebida2
from .views_agregar import agregar

app_name= 'tienda'

urlpatterns=[
    path("", EjemploTienda.as_view(), name="ejemplo_tienda"),
    path('verimagenes/', VerImagenes.as_view(), name="verimagenes"),
    path('<int:producto_id>/ver/', ver_imagen, name="ver"),
    path('agregar/', agregar, name="agregar"),
    path('usar_ajax/', para_ajax, name="usar_ajax"),
    path("buscar_bebida/", BuscarBebida.as_view(), name="buscar_bebida"),
    path("buscar_bebida2/", BuscarBebida2.as_view(), name="buscar_bebida2"),
    ]