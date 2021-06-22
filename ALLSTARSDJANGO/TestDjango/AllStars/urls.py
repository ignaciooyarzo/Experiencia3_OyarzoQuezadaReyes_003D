from django.urls import path
from .views import form_modificarconsulta, home, crearContacto, ventaArticulos,quienesSomos, form_borrarconsulta

urlpatterns=[
    path('home',home, name='home'),
    path('quienes_somos', quienesSomos, name='quienesSomos'),
    path('crear_contacto', crearContacto, name='crearContacto'),
    path('venta_articulos', ventaArticulos, name='ventaArticulos'),
    path('form_modificarconsulta/<id>', form_modificarconsulta, name='form_modificarconsulta'),
    path('form_borrarconsulta/<id>', form_borrarconsulta, name='form_borrarconsulta'),

]