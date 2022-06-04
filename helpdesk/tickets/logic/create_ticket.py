from django.shortcuts import redirect
from tickets.models import Tickets, TicketsMessage


def create_ticket(form):


    try:
        Tickets.objects.create(form)
        return redirect('tickets')
    except:
        form.add_error(None, 'Ошибка добовления поста')