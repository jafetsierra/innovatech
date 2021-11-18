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