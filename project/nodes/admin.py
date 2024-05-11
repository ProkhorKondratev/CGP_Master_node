from django.contrib import admin
from .models import WorkerNode


@admin.register(WorkerNode)
class WorkerNodeAdmin(admin.ModelAdmin):
    list_display = ('host', 'port', 'created_at', 'updated_at')
    search_fields = ('host', 'port', 'created_at', 'id')
    list_filter = ('created_at', 'updated_at')

    fieldsets = (
        (
            None,
            {
                'fields': (
                    ('id',),
                    'description',
                    'owner',
                    'host',
                    'port',
                )
            },
        ),
        (
            'Важные даты',
            {
                'fields': (
                    'created_at',
                    'updated_at',
                )
            },
        ),
    )
    readonly_fields = ('created_at', 'updated_at', 'id')
