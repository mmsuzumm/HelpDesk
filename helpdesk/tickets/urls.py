from django.urls import path

from . import views

urlpatterns = [
    path('tickets/', views.TicketsMainPage.as_view(), name='tickets'),
    path('index/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('settings/', views.settings, name='settings'),
    path('tickets/<slug:ticket_slug>', views.show_ticket, name='ticket'),
    path('support/', views.support, name='support'),
    path('create_new_ticket/', views.create_ticket, name='create_ticket')
]