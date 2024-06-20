from rest_framework.serializers import ModelSerializer
from .models import Worknode


class WorknodeSerializer(ModelSerializer):
    class Meta:
        model = Worknode
        fields = '__all__'
