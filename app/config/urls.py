from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from authentication import urls as auth_urls
from workspaces import urls as workspaces_urls
from worknodes import urls as worknodes_urls

# маршруты djangorestframework
router = DefaultRouter()

# подключение маршрутов модулей
router.registry.extend(workspaces_urls.view_sets)
router.registry.extend(worknodes_urls.view_sets)

# объявление стандартных маршрутов
urlpatterns = [
    path('auth/', include(auth_urls)),
    path('nodes/', include(worknodes_urls.urlpatterns)),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
