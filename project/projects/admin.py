from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'created_at', 'id')
    list_filter = ('created_at', 'updated_at')

    fieldsets = (
        (
            None,
            {
                'fields': (
                    ('id',),
                    'name',
                    'description',
                    'owner',
                    'coverage',
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
