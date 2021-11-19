from rest_framework import serializers
from productosApp.models.producto import Producto


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = [
            'name', 
            'description',
            'price',
            'category',
            #'thumbnail,'
            'stock',
        ]
    
    def to_representation(self,obj):
        
        producto = Producto.objects.get(id=obj.id)
        
        return {
            'name'          : producto.name,
            'description'   : producto.description,
            'price'         : producto.price,
            'category'      : producto.category,
            #'thumbanil': producto.thumbanil,
            'stock'         : producto.stock,
        }