from django.shortcuts import render
from rest_framework                    import generics, status
from rest_framework.response           import Response
from productosApp.models import Producto
from productosApp.serializers import ProductoSerializer

# Create your views here.
    
class ListProductoViews(generics.ListAPIView):
    serializer_class = ProductoSerializer
    
    def get_queryset(self):
        queryset = Producto.objects.filter(category=self.kwargs['category'])
        return queryset