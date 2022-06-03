# Generated by Django 4.0.4 on 2022-06-03 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('id_for_user', models.CharField(max_length=6, verbose_name='ticketID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('status', models.CharField(choices=[('Open', 'Open'), ('In progress', 'In progress'), ('Waiting for vendor', 'Waiting for vendor'), ('Waiting for client', 'Waiting for client'), ('Closed', 'Closed')], default='Open', max_length=30, verbose_name='Статус')),
                ('created_by', models.CharField(max_length=255, verbose_name='Создано')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
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
                ('updated_by', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='создано')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('which_ticket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.tickets')),
            ],
            options={
                'verbose_name_plural': 'Сообщения в тикетах',
                'ordering': ['created_at'],
            },
        ),
    ]
