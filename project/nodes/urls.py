from .views import WorkerNodeViewSet

view_sets = [
    (r'nodes', WorkerNodeViewSet, 'nodes'),
]
