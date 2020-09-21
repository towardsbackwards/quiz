from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from coreapp.models import CoreModel


class Account(CoreModel, AbstractUser):
    """Класс пользователя"""
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
    first_name = models.CharField('Имя пользователя', max_length=32, blank=True)