from helpdesk.tickets.models import Tickets

menu = [{'title': 'Главная', 'url_name': 'index'},
        {'title': 'Добавить тикет', 'url_name': 'create_ticket'},
        {'title': 'Поддержка', 'url_name': 'support'},
        {'title': 'Тикеты', 'url_name': 'tickets'},
        {'title': 'Настройки', 'url_name': 'settings'},
]

class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        tickets = Tickets.objects.all()
        context['menu'] = 'menu'
        context['tickets'] = tickets
        return context
