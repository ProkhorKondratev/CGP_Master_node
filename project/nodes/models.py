from django.contrib.gis.db import models
from django.conf import settings
import uuid


class WorkerNode(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name='Идентификатор',
        help_text='Уникальный идентификатор рабочего узла',
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Описание рабочего узла',
        blank=True,
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='worker_nodes',
        related_query_name='worker_node',
        verbose_name='Владелец',
        help_text='Владелец рабочего узла',
    )
    host = models.GenericIPAddressField(
        verbose_name='Хост',
        help_text='IP-адрес рабочего узла',
    )
    port = models.PositiveIntegerField(
        verbose_name='Порт',
        help_text='Порт рабочего узла',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        help_text='Дата создания рабочего узла',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления',
        help_text='Дата последнего обновления рабочего узла',
    )

    def __str__(self):
        return f'{self.host}:{self.port}'

    class Meta:
        verbose_name = 'Рабочий узел'
        verbose_name_plural = 'Рабочие узлы'
        ordering = ('-created_at',)
