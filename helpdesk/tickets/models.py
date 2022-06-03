from django.db import models
from django.urls import reverse


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
    status = models.CharField(max_length=255, default='In Progress', verbose_name='Статус')
    created_by = models.CharField(max_length=255, verbose_name='Создано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ticket', kwargs={'ticket_id': self.pk})

    class Meta:
        verbose_name = 'Tickets'
        verbose_name_plural = 'Тикеты'
