from django.urls import path

from homestart.apps import HomeConfig
from homestart.views import HomePageView, GuestPageView

app_name = HomeConfig.name

urlpatterns = [
    path('', GuestPageView.as_view(), name='quest'),
    path('home', HomePageView.as_view(), name='index'),
]