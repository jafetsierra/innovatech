from rest_framework import serializers
from registerApp.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',
                  'username',
                  'password',
                  'name',
                  'last_name',
                  'email',
                  'adress',
                  'cellphone'
                  ]
        def create(self, validated_data):
            userInstance = User.objects.create(**validated_data)
            
            return userInstance
        
        def to_representation(self, obj):
            user = User.objects.get(id=obj.id)

            return {
                'id': user.id,
                'username': user.username,
                'name': user.name,
                'email': user.email
            }