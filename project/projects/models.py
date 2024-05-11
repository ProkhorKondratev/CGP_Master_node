from django.contrib.gis.db import models
from django.conf import settings
import uuid


class Project(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name='Идентификатор',
        help_text='Уникальный идентификатор проекта',
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Название',
        help_text='Название проекта',
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Описание проекта',
        blank=True,
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='projects',
        related_query_name='project',
        verbose_name='Владелец',
        help_text='Владелец проекта',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        help_text='Дата создания проекта',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления',
        help_text='Дата последнего обновления проекта',
    )
    coverage = models.PolygonField(
        null=True,
        blank=True,
        verbose_name='Охват',
        help_text='Охват рабочей области проекта',
        srid=4326,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ('-created_at',)
