from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()

router.register('api/testpage', TestPage)

urlpatterns = [
    path('tickets/', Tickets.as_view(), name='tickets'),
    path('index/', index, name='home'),
    path('about/', about, name='about'),
    path('settings/', settings, name='settings'),
    path('tickets/<slug:ticket_slug>', show_ticket, name='ticket'),
    path('ticket/<slug:slug>', ShowTicket.as_view(), name='ticket'),
    path('support/', support, name='support'),
    path('create_new_ticket/', create_ticket, name='create_ticket'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]

urlpatterns += router.urls
