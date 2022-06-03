from django import template
from tickets.models import *

register = template.Library()

@register.simple_tag(name='menu')
def get_menu():
    menu = [
        {'title': 'Главная', 'url_name': 'home'},
        {'title': 'Тикеты', 'url_name': 'tickets'},
        {'title': 'Настройки', 'url_name': 'settings'},
        {'title': 'О нас', 'url_name': 'about'},
    ]
    return menu




@register.inclusion_tag('tickets/show_tickets.html')
def show_tickets():
    tickets = Tickets.objects.all()
    return {'tickets': tickets}
