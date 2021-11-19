from rest_framework                    import generics, status, views
from rest_framework.response           import Response
from productosApp.models import Producto
from productosApp.serializers.productoSerializer import ProductoSerializer

# Create your views here.
    
class ListProductoViews(generics.ListAPIView):
    serializer_class = ProductoSerializer
    
    def get_queryset(self):
        print(self.kwargs)
        queryset = Producto.objects#.filter(category=self.kwargs['category'])
        
        return queryset