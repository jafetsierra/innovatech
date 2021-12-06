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
        '''
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        #print("********************\n"*2,valid_data,"\n"*2)
        #print("\n"*2,kwargs,"\n"*2,"*********************")
        
        if valid_data['user_id'] != kwargs['user_id']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        request.data["userId"] = kwargs['user_id']
        '''
        request.data["userId"] = kwargs['user_id']
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Medio de pago añadido'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)