from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from projects.urls import view_sets as projects_view_sets
from nodes.urls import view_sets as nodes_view_sets

router = DefaultRouter()
router.registry.extend(projects_view_sets)
router.registry.extend(nodes_view_sets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
