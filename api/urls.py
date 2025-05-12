from django.urls import path
from .views import ClienteListCreateView, ClienteDetailView,ProveedorDetailView,ProveedorListCreateView, ProductoDetailView,ProductoListCreateView

urlpatterns = [
    path('cliente/', ClienteListCreateView.as_view(), name='cliente-listar-crear'),
    path('cliente/<int:pk>/', ClienteDetailView.as_view(), name='cliente-editar-actualizar'),
    path('proveedor/', ProveedorListCreateView.as_view(), name='proveedor-listar-crear'),
    path('proveedor/<int:pk>/', ProveedorDetailView.as_view(), name='proveedor-editar-actualizar'), 
    path('producto/', ProductoListCreateView.as_view(), name='producto-listar-crear'),
    path('producto/<int:pk>/', ProductoDetailView.as_view(), name='producto-editar-actualizar'), 
]