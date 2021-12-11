from rest_framework                    import status, views, generics
from rest_framework.response           import Response
from rest_framework.permissions        import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from django.conf import settings

from mediopagoApp.models import Medio
from mediopagoApp.serializers.medioSerializer import MedioSerializer
from registerApp.models.user import User

class MedioCreateView(generics.CreateAPIView):
    queryset = Medio.objects.all()
    serializer_class = MedioSerializer
    #permission_classes = (IsAuthenticated,)
    
    def post(self,request, *args, **kwargs):
    
        request.data["userId"] = kwargs['pk']
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Medio de pago añadido'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)