# Generated by Django 4.0.5 on 2022-06-20 05:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('id_for_user', models.CharField(max_length=6, unique=True, verbose_name='ticketID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('status', models.CharField(choices=[('Open', 'Open'), ('In progress', 'In progress'), ('Waiting for vendor', 'Waiting for vendor'), ('Waiting for client', 'Waiting for client'), ('Closed', 'Closed')], default='Open', max_length=30, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ticket_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_edit_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_ticket_editor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tickets',
                'verbose_name_plural': 'Тикеты',
            },
        ),
        migrations.CreateModel(
            name='TicketsMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='содержимое')),
                ('photo', models.ImageField(upload_to='photos/%Y/m%/%d/')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='создано')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='message_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_edit_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_message_editor', to=settings.AUTH_USER_MODEL)),
                ('which_ticket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.tickets')),
            ],
            options={
                'verbose_name_plural': 'Сообщения в тикетах',
                'ordering': ['created_at'],
            },
        ),
    ]
