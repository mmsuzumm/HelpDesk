from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from .status import status


class TicketsMessage(models.Model):  # Само наполнение тикетов
    which_ticket = models.ForeignKey('Tickets', on_delete=models.CASCADE, null=True)
    content = models.TextField(blank=False, verbose_name='содержимое')
    photo = models.ImageField(upload_to='photos/%Y/m%/%d/')
    created_by = models.ForeignKey(User, related_name='message_created_by', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создано')
    updated_at = models.DateTimeField(auto_now=True)
    last_edit_user = models.ForeignKey(User, related_name='last_message_editor', on_delete=models.SET_NULL, null=True)

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
    last_edit_user = models.ForeignKey(User, related_name='last_ticket_editor', on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(User, related_name='ticket_created_by', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ticket', kwargs={'ticket_slug': self.slug})

    class Meta:
        verbose_name = 'Tickets'
        verbose_name_plural = 'Тикеты'
