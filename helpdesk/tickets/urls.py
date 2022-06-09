from django.urls import path

from . import views

urlpatterns = [
    path('tickets/', views.Tickets.as_view(), name='tickets'),
    path('index/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('settings/', views.settings, name='settings'),
    path('tickets/<slug:ticket_slug>', views.show_ticket, name='ticket'),
    path('ticket/<slug:slug>', views.ShowTicket.as_view(), name='ticket'),
    path('support/', views.support, name='support'),
    path('create_new_ticket/', views.create_ticket, name='create_ticket')
]