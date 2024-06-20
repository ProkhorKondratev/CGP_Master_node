from .views import WorkspaceViewSet

view_sets = [
    (r'workspaces', WorkspaceViewSet, 'workspace'),
]
