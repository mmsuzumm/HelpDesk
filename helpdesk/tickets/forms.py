from django import forms
from django.forms import inlineformset_factory

from .models import Tickets, TicketsMessage


class AddTicketsMessageForm(forms.ModelForm):
    class Meta:
        model = TicketsMessage
        fields = ['content', ]


class AddTicketForm(AddTicketsMessageForm):
    class Meta(AddTicketsMessageForm.Meta):
        model = Tickets
        fields = ['title', 'id_for_user', 'status', 'created_by']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.TextInput(attrs={'cols': 60, 'rows': 10}),
        }


class AddMessageForm(forms.ModelForm):
    class Meta:
        model = TicketsMessage
        fields = ['content', ]
        widgets = {
            'content': forms.TextInput(attrs={'cols': 60, 'rows': 10,}),
        }