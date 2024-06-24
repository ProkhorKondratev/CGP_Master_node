import aiohttp
import asyncio
from asgiref.sync import sync_to_async
from django.http import JsonResponse
from django.views import View
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from utils.filters import OwnerFilterBackend
from .models import Workspace
from worknodes.models import Worknode
from .serializers import WorkspaceSerializer


class WorkspaceViewSet(ModelViewSet):
    queryset = Workspace.objects.all()

    serializer_class = WorkspaceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [OwnerFilterBackend]
    filterset_fields = ['owner']


class GeoDataCentroidsView(View):
    async def get(self, request):
        user = await request.auser()
        nodes = await sync_to_async(list)(Worknode.objects.filter(owner=user))

        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_geo_data(session, node) for node in nodes]
            results = await asyncio.gather(*tasks)

        return JsonResponse(results, safe=False)

    async def fetch_geo_data(self, session, node: Worknode):
        url = f"http://{node.host}:{node.port}/geodata/centroids"
        async with session.get(url) as response:
            data = await response.json()

class GeoDataView(View):
    async def get(self, request, workspace_id):
        user = await request.auser()
        workspace = await sync_to_async(Workspace.objects.get)(id=workspace_id)
        nodes = await sync_to_async(list)(Worknode.objects.filter(owner=user))

        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_geo_data(session, node, workspace) for node in nodes]
            results = await asyncio.gather(*tasks)

        return JsonResponse(results, safe=False)

    async def fetch_geo_data(self, session, node: Worknode, workspace: Workspace):
        coverage = workspace.coverage.json()
        url = f"http://{node.host}:{node.port}/geodata/by_coverage"
        async with session.post(url, json=coverage) as response:
            data = await response.json()

