from django.contrib import admin
from .models import Workspace


@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'owner')
    list_filter = ('owner',)

    fieldsets = (
        ('Информация', {'fields': ('name',)}),
        (
            'Пользователь',
            {
                'fields': ('owner',),
            },
        ),
    )
