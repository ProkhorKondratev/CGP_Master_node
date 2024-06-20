from django.conf import settings
from django.db import models
from app.utils.mixins import TimestampedModel
import uuid


class Worknode(TimestampedModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name='Идентификатор',
        help_text='Уникальный идентификатор рабочего узла',
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

    def __str__(self):
        return f'{self.host}:{self.port}'

    class Meta:
        verbose_name = 'Рабочий узел'
        verbose_name_plural = 'Рабочие узлы'
        ordering = ('-created_at',)
