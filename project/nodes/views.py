from rest_framework.viewsets import ModelViewSet
from .models import WorkerNode
from .serializers import WorkerNodeSerializer


class WorkerNodeViewSet(ModelViewSet):
    queryset = WorkerNode.objects.all()
    serializer_class = WorkerNodeSerializer

    def get_queryset(self):
        return WorkerNode.objects.all()
