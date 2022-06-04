from django import forms
from .models import Tickets, TicketsMessage
from .status import status


class AddTicketForm(forms.Form):
    title = forms.CharField(max_length=30, label='Опишите суть проблемы', widget=forms.TextInput(attrs=dict(
        placeholder='Ничего не работает')))
    id_for_user = forms.SlugField(max_length=6, label='Тикет ID', widget=forms.TextInput(attrs=dict(
        placeholder='1DP3AC')))
    status = forms.ChoiceField(choices=status(), label='Status')
    content = forms.CharField(widget=forms.Textarea(attrs=dict({'cols': 60, 'rows': 10}, placeholder='Все сломалось')),
                              label='Опишите проблему')
    created_by = forms.CharField(max_length=30, label='Задача от',
                                 widget=forms.TextInput(attrs=dict(placeholder='admin')))
