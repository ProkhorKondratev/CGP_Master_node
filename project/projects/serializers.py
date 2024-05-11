from rest_framework_gis.serializers import ModelSerializer
from .models import Project


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        geo_field = 'coverage'
