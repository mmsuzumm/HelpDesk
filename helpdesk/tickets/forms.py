from django import forms
from .models import Tickets, TicketsMessage
from .status import status


class AddTicketForm(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ['title', 'id_for_user', 'status', 'created_by']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.TextInput(attrs={'cols': 60, 'rows': 10}),  #                        Вот тут. Очень странно
        }                                                                #                           ^
                                                                         #                           |
                                                                         #                           |
class AddTicketsMessageForm(forms.ModelForm):                            #                           |
    class Meta:                                                          #                           |
        model = TicketsMessage                                           #                           |
        fields = ['content', ]                                           # Вот это отрисовывается    |


class AddMessageForm(forms.ModelForm):
    class Meta:
        model = TicketsMessage
        fields = ['content', ]
        widgets = {
            'content': forms.TextInput(attrs={'cols': 60, 'rows': 10,}),
        }