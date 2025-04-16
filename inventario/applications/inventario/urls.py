from django.urls import path
from . import views

app_name = "inventario_app"

urlpatterns = [
    path(
        'add-inventario/',
        views.InventarioCreateView.as_view(),
        name= "add-inventario"
    ),
    path(
        'lista-inventario/',
        views.InventarioListView.as_view(),
        name= "lista-inventario"
    ),
    path(
        'detalle-equipo/<pk>',
        views.InventarioDetailView.as_view(),
        name= "detalle-equipo"
    ),
    path(
        'reporte-equipos/<int:equipo_id>/', 
        views.generar_pdf_equipo, 
        name='reporte_equipo'
    ),
]