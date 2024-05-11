from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    empty_value_display = 'Не указано'

    fieldsets = (
        (
            None,
            {'fields': ('username', 'password')},
        ),
        (
            'Персональная информация',
            {
                'fields': (
                    ('last_name', 'first_name'),
                    ('middle_name',),
                    ('email', 'phone'),
                )
            },
        ),
        (
            'Права доступа',
            {
                'classes': ('collapse',),
                'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
            },
        ),
        (
            'Важные даты',
            {
                'classes': ('collapse',),
                'fields': ('last_login', 'date_joined'),
            },
        ),
    )

    list_display = (
        'username',
        'email',
        'fio',
        'phone',
    )
    list_display_links = ('username', 'email')

    @admin.display(description='ФИО')
    def fio(self, obj):
        return obj.get_full_name()
