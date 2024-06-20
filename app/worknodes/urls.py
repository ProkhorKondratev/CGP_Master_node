from .views import WorknodeViewSet

view_sets = [
    (r'worknodes', WorknodeViewSet, 'worknode'),
]
