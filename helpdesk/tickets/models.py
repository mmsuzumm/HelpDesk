from django.db import models


class Tickets(models.Model):  # Каждый тикет
    title = models.CharField(max_length=255)
    updated_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Ticket(models.Model):  # Само наполнение тикетов
    content = models.TextField(blank=False)
    updated_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    which_ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE)

    def __str__(self):
        return self.which_ticket
