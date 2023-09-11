from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingCreateView, MailingListView, ClientCreateView, ClientListView, MailingUpdateView, \
    MailingDeleteView, ClientDeleteView, ClientUpdateView

app_name = MailingConfig.name


urlpatterns = [
    path('', MailingListView.as_view(), name='mailing_list'),
    path('create', MailingCreateView.as_view(), name='mailing_create'),
    path('update/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
    path('delete/<int:pk>', MailingDeleteView.as_view(), name='mailing_delete'),

    path('client_create', ClientCreateView.as_view(), name='client_create'),
    path('client_list', ClientListView.as_view(), name='client_list'),
    path('client_delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),
    path('client_update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
]