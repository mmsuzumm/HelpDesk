from django.shortcuts import redirect

from .forms import AddTicketForm, AddTicketsMessageForm
from .models import Tickets as TicketsModel, TicketsMessage as TicketsMessageModel

def create_ticket_logic(request):

    form_ticket = AddTicketForm(request.POST)
    form_message = AddTicketsMessageForm(request.POST)
    if form_ticket.is_valid() and form_message.is_valid():
        form_message = form_message.cleaned_data
        form_ticket = form_ticket.cleaned_data
        form_ticket['slug'] = form_ticket.get('id_for_user')
        try:
            temp_obj = TicketsModel.objects.create(**form_ticket)
            form_message['which_ticket'] = temp_obj
            TicketsMessageModel.objects.create(**form_message)
            return redirect('tickets')
        except Exception as e:
            form_ticket.add_error(None, f'Ошибка: {e}')