from django.contrib import admin
from .models import Worknode


@admin.register(Worknode)
class WorkNodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'host', 'port', 'owner')
    list_display_links = ('id', 'host')
    search_fields = ('host', 'owner')
    list_filter = ('owner',)

    fieldsets = (
        ('Подключение', {'fields': ('host', 'port')}),
        (
            'Информация',
            {
                'fields': ('owner',),
            },
        ),
    )
