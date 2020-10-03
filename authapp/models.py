from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from coreapp.models import CoreModel


class Account(CoreModel, AbstractUser):
    """Расширенный класс пользователя"""
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
    first_name = models.CharField('Имя пользователя', max_length=32, blank=True)
    objects = UserManager()

    def __str__(self):
        return f'{self.username} (id={self.id})'
