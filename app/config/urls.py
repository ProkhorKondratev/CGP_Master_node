from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from authentication import urls as auth_urls
from workspaces.urls import view_sets as workspaces_urls
from worknodes.urls import view_sets as worknodes_urls


router = DefaultRouter()
router.registry.extend(workspaces_urls)
router.registry.extend(worknodes_urls)


urlpatterns = [
    path('auth/', include(auth_urls)),
    # path('worknodes/', include(worknodes_urls)),
    # path('workspaces/', include(workspaces_urls)),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
