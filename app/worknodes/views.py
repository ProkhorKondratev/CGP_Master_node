import aiohttp
import asyncio
from asgiref.sync import sync_to_async
from django.http import JsonResponse
from django.views import View
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


class NodeInfoView(View):
    async def get(self, request):
        user = await request.auser()
        nodes = await sync_to_async(list)(Worknode.objects.filter(owner=user))

        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_info(session, node) for node in nodes]
            results = await asyncio.gather(*tasks)

        return JsonResponse(results, safe=False)

    async def fetch_info(self, session, node: Worknode):
        url = f"http://{node.host}:{node.port}/info"
        async with session.get(url) as response:
            data = await response.json()
            return {
                "id": node.id,
                'host': node.host,
                'port': node.port,
                'cpu': data['cpu'],
                'memory': data['memory'],
                'disk': data['disk'],
                'gpu': data['gpu'],
                'status': data['status'],
                'version': data['version'],
                'description': data['description'],
            }
