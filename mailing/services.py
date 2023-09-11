from django.conf import settings
from django.core.mail import send_mail


def send_email(mailing, client):
    return send_mail(
        subject=mailing.title,
        message=mailing.body,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[client.email],
        fail_silently=False
    )