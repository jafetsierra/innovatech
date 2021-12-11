from rest_framework                    import status, views, generics
from rest_framework.response           import Response
from rest_framework.permissions        import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from django.conf import settings
from mediopagoApp.models.medio import Medio
from mediopagoApp.serializers.medioSerializer import MedioSerializer
from registerApp.models.user import User

class MedioDeleteView(generics.DestroyAPIView):
    queryset = Medio.objects.all()
    serializer_class = MedioSerializer
    
    #lookup_field = ('userId')
    def get_queryset(self):
              
        queryset = Medio.objects.filter(userId=self.kwargs['pk'], id=self.request.data['id'])
        return queryset