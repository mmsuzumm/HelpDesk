from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views
from .views import TestPage

router = SimpleRouter()

router.register('api/testpage', TestPage)

urlpatterns = [
    path('tickets/', views.Tickets.as_view(), name='tickets'),
    path('index/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('settings/', views.settings, name='settings'),
    path('tickets/<slug:ticket_slug>', views.show_ticket, name='ticket'),
    path('ticket/<slug:slug>', views.ShowTicket.as_view(), name='ticket'),
    path('support/', views.support, name='support'),
    path('create_new_ticket/', views.create_ticket, name='create_ticket'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register')
]

urlpatterns += router.urls
