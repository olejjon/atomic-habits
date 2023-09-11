import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='o.bolibok@yandex.ru',
            first_name='admin',
            last_name='admin',
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )

        user.set_password('123')#os.getenv('ADMIN_PASS'))
        user.save()
