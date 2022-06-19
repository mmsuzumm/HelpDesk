from django import template
register = template.Library()


@register.simple_tag(name='menu')
def get_menu():
    menu = [
        {'title': 'Главная', 'url_name': 'home'},
        {'title': 'Тикеты', 'url_name': 'tickets'},
        {'title': 'Настройки', 'url_name': 'settings'},
        {'title': 'О нас', 'url_name': 'about'},
        {'title': 'Поддержка', 'url_name': 'support'},
        {'title': 'Войти', 'url_name': 'login'}
    ]
    return menu
