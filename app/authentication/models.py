from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    middle_name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name='Отчество',
        help_text='При наличии',
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        if not self.first_name:
            return self.username
        if not self.last_name:
            return self.first_name
        if not self.middle_name:
            return f'{self.first_name} {self.last_name[0]}.'
        return f'{self.last_name} {self.first_name[0]}. {self.middle_name[0]}.'
