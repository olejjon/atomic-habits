from django import forms

from mailing.mailing_models import Mailing


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['title', 'body', 'mailing_time', 'frequency', 'clients']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'mailing_time': forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'class': 'form-control'}),
            'frequency': forms.Select(attrs={'class': 'form-control'}),
        }