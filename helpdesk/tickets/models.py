from django.db import models
from django.urls import reverse


class Tickets(models.Model):  # Каждый тикет
    title = models.CharField(max_length=255)
    updated_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_ticket', kwargs={'ticket_id': self.title})


class Ticket(models.Model):  # Само наполнение тикетов
    content = models.TextField(blank=False)
    updated_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    which_ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.which_ticket

