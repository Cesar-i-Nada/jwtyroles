from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Cliente, Proveedor, Producto, Empleado, MetodoPago, Pedido, PedidoProducto
from .serializers import ClienteSerializer, ProveedorSerializer, ProductoSerializer, EmpleadoSerializer, MetodoPagoSerializer, PedidoSerializer, PedidoProductoSerializer

from rest_framework.permissions import BasePermission, IsAuthenticated

#Esta clase es para verificar al usuario con permisos de admin 
class IsAdminUserGroup(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='admin').exists()

class ClienteListCreateView(ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer 
    
class ClienteDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
        
class ProveedorListCreateView(ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    
class ProveedorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    
class ProductoListCreateView(ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
class ProductoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer    
    
class EmpleadoListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUserGroup, IsAuthenticated]
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    
class EmpleadoDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserGroup, IsAuthenticated]
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    
class MetodoPagoListCreateView(ListCreateAPIView):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodoPagoSerializer
    
class MetodoPagoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodoPagoSerializer
    
class PedidoListCreateView(ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    
class PedidoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    
class PedidoProductoListCreateView(ListCreateAPIView):
    queryset = PedidoProducto.objects.all()
    serializer_class = PedidoProductoSerializer
    
class PedidoProductoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = PedidoProducto.objects.all()
    serializer_class = PedidoProductoSerializer    