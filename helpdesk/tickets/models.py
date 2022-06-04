from django.db import models
from django.urls import reverse
from .status import status
STATUS = (('Open', 'Open'), ('In progress', 'In progress'),
          ('Waiting for vendor', 'Waiting for vendor'),
          ('Waiting for client', 'Waiting for client'), ('Closed', 'Closed')
          )


class TicketsMessage(models.Model):  # Само наполнение тикетов
    content = models.TextField(blank=False, verbose_name='содержимое')
    updated_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создано')
    updated_at = models.DateTimeField(auto_now=True)
    which_ticket = models.ForeignKey('Tickets', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = 'Сообщения в тикетах'
        ordering = ['created_at']


class Tickets(models.Model):  # Каждый тикет
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    id_for_user = models.CharField(max_length=6, verbose_name='ticketID', unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    status = models.CharField(max_length=30, default='Open', choices=status(), verbose_name='Статус')
    created_by = models.CharField(max_length=255, verbose_name='Создано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ticket', kwargs={'ticket_slug': self.slug})

    class Meta:
        verbose_name = 'Tickets'
        verbose_name_plural = 'Тикеты'
