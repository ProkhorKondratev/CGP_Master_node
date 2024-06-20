from asgiref.sync import sync_to_async
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json


class GetCSRFTokenView(View):
    async def get(self, request):
        return JsonResponse({'csrfToken': get_token(request)})


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    async def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        if username is None or password is None:
            return JsonResponse({'detail': 'Пожалуйста предоставьте логин и пароль'}, status=400)

        user = await sync_to_async(authenticate)(username=username, password=password)
        if user is None:
            return JsonResponse({'detail': 'Неверные данные'}, status=400)

        await sync_to_async(login)(request, user)
        return JsonResponse({'detail': 'Успешная авторизация'})


class LogoutView(View):
    async def get(self, request):
        await sync_to_async(logout)(request)
        return JsonResponse({'detail': 'Вы успешно вышли'})


class CheckAuthView(View):
    async def get(self, request):
        if request.user.is_authenticated:
            return JsonResponse({'isAuthenticated': True, 'username': request.user.username})
        return JsonResponse({'isAuthenticated': False})
