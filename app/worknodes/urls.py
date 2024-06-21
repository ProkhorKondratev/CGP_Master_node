from django.urls import path
from .views import WorknodeViewSet, NodeInfoView

view_sets = [
    (r'worknodes', WorknodeViewSet, 'worknode'),
]

urlpatterns = [
    path('info/', NodeInfoView.as_view(), name='node-info'),
]
