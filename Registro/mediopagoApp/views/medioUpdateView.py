from rest_framework                    import status, views, generics
from rest_framework.response           import Response
from rest_framework.permissions        import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from django.conf import settings
from mediopagoApp.models.medio import Medio
from mediopagoApp.serializers.medioSerializer import MedioSerializer
from registerApp.models.user import User

class MedioUpdateView(generics.UpdateAPIView):
    queryset = Medio.objects.all()
    serializer_class = MedioSerializer
    #permission_classes = (IsAuthenticated,)
    lookup_field = ('userId')
    def get_queryset(self):
        '''
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        print("********************\n"*2,valid_data,"\n"*2)
        print("\n"*2,self.kwargs,"\n"*2,"*********************")
        
        if valid_data['user_id'] != self.kwargs['userId']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        #print(self.request.data)
        '''
        
        self.request.data["userId"] = self.kwargs['userId']
        queryset = Medio.objects.filter(userId=self.kwargs['userId'], id=self.request.data['id'])
        return queryset