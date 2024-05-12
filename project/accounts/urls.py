from django.urls import path
from .views import get_csrf, login_view, logout_view, check_auth

urlpatterns = [
    path('csrf/', get_csrf, name='api-csrf'),
    path('login/', login_view, name='api-login'),
    path('logout/', logout_view, name='api-logout'),
    path('check-auth/', check_auth, name='api-check-auth'),
]
