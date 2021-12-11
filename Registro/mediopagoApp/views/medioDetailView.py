from rest_framework                    import status, views, generics
from rest_framework.response           import Response
from rest_framework.permissions        import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from django.conf import settings
from mediopagoApp.models.medio import Medio
from mediopagoApp.serializers.medioSerializer import MedioSerializer
from registerApp.models.user import User

class MedioListView(generics.ListAPIView):

    queryset = Medio.objects.all()
    serializer_class = MedioSerializer
    def get_queryset(self):
        queryset = Medio.objects.filter(userId=self.kwargs['pk'])
        return queryset
