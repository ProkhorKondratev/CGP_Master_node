from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from utils.filters import OwnerFilterBackend
from .models import Worknode
from .serializers import WorknodeSerializer


class WorknodeViewSet(ModelViewSet):
    queryset = Worknode.objects.all()

    serializer_class = WorknodeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [OwnerFilterBackend]
    filterset_fields = ['owner']
