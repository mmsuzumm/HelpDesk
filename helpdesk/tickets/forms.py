from django import forms
from .models import Tickets, TicketsMessage
from .status import status


class AddTicketForm(forms.Form):
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255)
    title = forms.CharField(max_length=30)
    content = forms.CharField()
