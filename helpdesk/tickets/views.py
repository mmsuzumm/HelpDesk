from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import *

status_menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Тикеты', 'url_name': 'tickets'},
    {'title': 'Настройки', 'url_name': 'settings'}]


def index(request):
    tickets_params = Tickets.objects.all()
    context = {
        'title': 'Главная страница',
        'status_menu': status_menu
    }
    return render(request, 'tickets/index.html', context=context)


def about(request):
    return render(request, 'tickets/about.html', {
        'title': 'О сайте',
        'status_menu': status_menu
    })


def show_ticket(request, ticket_id):
    return HttpResponse(f'Отображение тикета с названием: {ticket_id}')


def tickets(request):
    tickets_params = Tickets.objects.all()
    context = {
        'title': 'Тикеты',
        'tickets_params': tickets_params,
    }
    return render(request, 'tickets/tickets.html', context=context)


def settings(request):
    return HttpResponse('Настройки')
