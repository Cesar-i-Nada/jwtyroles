from django.urls import path
from .views import ClienteListCreateView, ClienteDetailView,ProveedorListCreateView, ProveedorDetailView,ProductoListCreateView,ProductoDetailView, EmpleadoListCreateView,EmpleadoDetailView,MetodoPagoListCreateView, MetodoPagoDetailView, PedidoListCreateView,PedidoDetailView, PedidoProductoListCreateView, PedidoProductoDetailView

urlpatterns = [
    path('cliente/', ClienteListCreateView.as_view(), name='cliente-listar-crear'),
    path('cliente/<int:pk>/', ClienteDetailView.as_view(), name='cliente-editar-actualizar'),
    path('proveedor/', ProveedorListCreateView.as_view(), name='proveedor-listar-crear'),
    path('proveedor/<int:pk>/', ProveedorDetailView.as_view(), name='proveedor-editar-actualizar'), 
    path('producto/', ProductoListCreateView.as_view(), name='producto-listar-crear'),
    path('producto/<int:pk>/', ProductoDetailView.as_view(), name='producto-editar-actualizar'), 
    path('empleado/', EmpleadoListCreateView.as_view(), name='empleado-listar-crear'),
    path('empleado/<int:pk>/', EmpleadoDetailView.as_view(), name='empleado-editar-actualizar'),
    path('metodoPago/', MetodoPagoListCreateView.as_view(), name='metodoPago-listar-crear'),
    path('metodoPago/<int:pk>/', MetodoPagoDetailView.as_view(), name='metodoPago-editar-actualizar'),
    path('pedido/', PedidoListCreateView.as_view(), name='pedido-listar-crear'),
    path('pedido/<int:pk>/', PedidoDetailView.as_view(), name='pedido-editar-actualizar'),
    path('pedidoProducto/', PedidoProductoListCreateView.as_view(), name='pedidoProducto-listar-crear'),
    path('pedidoProducto/<int:pk>/', PedidoProductoDetailView.as_view(), name='pedidoProducto-editar-actualizar'),
]