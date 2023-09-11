from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Mailing(models.Model):
    class Frequency(models.TextChoices):
        DAILY = 'daily', 'Раз в день'
        WEEKLY = 'weekly', 'Раз в неделю'
        MONTHLY = 'monthly', 'Раз в месяц'

    class Status(models.TextChoices):
        COMPLETED = 'completed', 'Завершена'
        CREATED = 'created', 'Создана'
        STARTED = 'started', 'Запущена'

    mailing_time = models.DateTimeField(verbose_name='mailing_time')
    frequency = models.CharField(max_length=15,
                                 choices=Frequency.choices,
                                 default=Frequency.DAILY,
                                 verbose_name='frequency',
                                 )
    status = models.CharField(max_length=15,
                              choices=Status.choices,
                              default=Status.CREATED,
                              verbose_name='status',
                              )
    title = models.CharField(max_length=100, verbose_name='title')
    body = models.TextField(**NULLABLE, verbose_name='body')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='user')
    clients = models.ManyToManyField('mailing.Client', verbose_name='clients')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Mailing'
        verbose_name_plural = 'Mailings'