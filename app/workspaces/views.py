from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from utils.filters import OwnerFilterBackend
from .models import Workspace
from .serializers import WorkspaceSerializer


class WorkspaceViewSet(ModelViewSet):
    queryset = Workspace.objects.all()

    serializer_class = WorkspaceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [OwnerFilterBackend]
    filterset_fields = ['owner']
