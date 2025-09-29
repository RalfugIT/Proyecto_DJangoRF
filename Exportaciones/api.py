from .models import Embarque, Operacion
from rest_framework import viewsets, permissions
from .serializers import EmbarqueSerializer

class EmbarqueViewSet(viewsets.ModelViewSet):
    queryset = Embarque.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EmbarqueSerializer