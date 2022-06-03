# Generated by Django 4.0.4 on 2022-06-02 10:15

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
                ('created_by', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
            ],
            options={
                'verbose_name': 'Tickets',
                'verbose_name_plural': 'Tickets',
            },
        ),
        migrations.CreateModel(
            name='TicketsMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('updated_by', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('which_ticket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.tickets')),
            ],
            options={
                'verbose_name_plural': 'TicketsMessage',
                'ordering': ['created_at'],
            },
        ),
    ]
