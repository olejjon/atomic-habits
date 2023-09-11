from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='user/', **NULLABLE, verbose_name='аватар')
    phone = models.IntegerField(**NULLABLE, verbose_name='телефон')
    country = models.CharField(**NULLABLE, max_length=100, verbose_name='страна')
    is_active = models.BooleanField(default=False, verbose_name='активность')
    verification_key = models.IntegerField(**NULLABLE, verbose_name='ключ')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
