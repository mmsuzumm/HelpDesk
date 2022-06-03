from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Tickets, TicketsMessage
from .forms import AddTicketForm


def index(request):  # name=home
    context = {
        'title': 'Главная страница',
    }
    return render(request, 'tickets/index.html', context=context)


def about(request):
    return render(request, 'tickets/about.html', {
        'title': 'О сайте',
    })


def tickets(request):
    tickets_params = Tickets.objects.all()
    form = AddTicketForm()
    context = {
        'form': form,
        'title': 'Тикеты',
        'tickets_params': tickets_params,
    }
    return render(request, 'tickets/tickets.html', context=context)


def settings(request):
    return render(request, 'tickets/settings.html', {
        'title': 'Настройки',
    })


def show_ticket(request, ticket_slug):
    post = get_object_or_404(Tickets, slug=ticket_slug)
    messages = TicketsMessage.objects.all()
    context = {
        'post': post,
        'title': post.title,
        'messages': messages,
    }
    return render(request, 'tickets/show_ticket.html', context=context)


def support(request):
    context = {
        'title': 'Поддержка'
    }
    return render(request, 'tickets/support.html', context=context)

