from django.db.models import fields
from rest_framework import serializers
from mediopagoApp.models import Medio

class MedioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medio
        fields = [
            'id',
            'userId',
            'type',
            'number',
            'expDate',
            'cv'
        ]
        
    def to_representation(self,obj):
        
        medio = Medio.objects.get(id=obj.id)
        
        return {
            'id,'       : medio.id,
            'userId'    : medio.userId,
            'type'      : medio.type,
            'number'    : medio.number,
            'expDate'   : medio.expDate,
            'cv'        : medio.cv
        }