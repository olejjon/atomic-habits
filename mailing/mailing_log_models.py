from django.db import models

NULLABLE = {'blank': True, 'null': True}


class MailingLog(models.Model):
    class AttemptStatus(models.TextChoices):
        SUCCESSFULLY = 'successfully', 'Успешно'
        NOT_SUCCESSFULLY = 'not successfully', 'Не успешно'

    last_try_datetime = models.DateTimeField(auto_now_add=True, verbose_name='last_try_datetime')
    attempt_status = models.CharField(choices=AttemptStatus.choices,
                                      default=AttemptStatus.SUCCESSFULLY,
                                      max_length=20,
                                      verbose_name='attempt_status'
                                      )
    server_response = models.TextField(**NULLABLE, verbose_name='server_response')
    mailing = models.ForeignKey('mailing.Mailing', on_delete=models.CASCADE, verbose_name='mailing')