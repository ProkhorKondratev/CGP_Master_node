import json
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.http import require_POST


def get_csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})


@require_POST
def login_view(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    # Валидация
    if username is None or password is None:
        return JsonResponse({'detail': 'Пожалуйста предоставьте логин и пароль'}, status=400)

    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse({'detail': 'Неверные данные'}, status=400)

    login(request, user)
    return JsonResponse({'detail': 'Успешная авторизация'})


def logout_view(request):
    logout(request)
    return JsonResponse({'detail': 'Вы успешно вышли'})


def check_auth(request):
    if request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': True, 'username': request.user.username})
    return JsonResponse({'isAuthenticated': False})
