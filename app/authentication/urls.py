from django.urls import path
from .views import GetCSRFTokenView, LoginView, LogoutView, CheckAuthView

urlpatterns = [
    path('csrf/', GetCSRFTokenView.as_view(), name='csrf_token'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('check-auth/', CheckAuthView.as_view(), name='check_auth'),
]
