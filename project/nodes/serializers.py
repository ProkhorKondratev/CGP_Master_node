from rest_framework.serializers import ModelSerializer
from .models import WorkerNode


class WorkerNodeSerializer(ModelSerializer):
    class Meta:
        model = WorkerNode
        fields = '__all__'
