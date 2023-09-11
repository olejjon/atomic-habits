from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(verbose_name='почта', unique=True)
    first_name = models.CharField(verbose_name='имя', max_length=50)
    last_name = models.CharField(verbose_name='фамилия', max_length=50)
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)
    user = models.ForeignKey('users.User', verbose_name='пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'