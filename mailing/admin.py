from django.contrib import admin

from mailing.client_models import Client
from mailing.mailing_log_models import MailingLog
from mailing.mailing_models import Mailing


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)


@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'server_response',)
    list_filter = ('mailing',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'user',)
    list_filter = ('user',)
    search_fields = ('email', 'user')