from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('settings/', views.settings, name='settings'),
    path('tickets/', views.tickets, name='tickets'),
    path('tickets/<slug:ticket_slug>', views.show_ticket, name='ticket'),
    path('support', views.support, name='support'),
]