from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from rest_framework.viewsets import ModelViewSet

from .logic import create_ticket_logic
from .models import Tickets as TicketsModel, TicketsMessage as TicketsMessageModel
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from .utils import DataMixin

from .serializers import TicketsSerializer


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'tickets/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super.get_context_date(**kwargs)
        return context


class Tickets(ListView):
    paginate_by = 5
    model = TicketsModel
    template_name = 'tickets/tickets.html'
    context_object_name = 'tickets_params'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_ticket'] = 'create_ticket'
        context['title'] = 'Тикеты'
        return context

    def get_queryset(self):
        return TicketsModel.objects.exclude(status='Closed')


class ShowTicket(DetailView):
    model = AddTicketForm
    template_name = 'tickets/show_ticket.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = TicketsMessageModel.objects.filter(which_ticket=
                                                                 self.model.objects.get(slug=self.kwargs['slug']))
        return context

def create_ticket(request):
    if request.method == 'POST':
        create_ticket_logic()
    else:
        form_ticket = AddTicketForm()
        form_message = AddTicketsMessageForm()
    context = {
        'form_ticket': form_ticket,
        'form_message': form_message,
    }
    return render(request, 'tickets/create_ticket.html', context=context)


def show_ticket(request, ticket_slug):
    post = get_object_or_404(TicketsModel, slug=ticket_slug)
    messages = TicketsMessageModel.objects.filter(which_ticket=post)
    context = {
        'slug': post.slug,
        'title': post.title,
        'messages': messages,
    }
    return render(request, 'tickets/show_ticket.html', context=context)


def index(request):  # name=home
    context = {
        'title': 'Главная страница',
    }
    return render(request, 'tickets/index.html', context=context)


def about(request):
    return render(request, 'tickets/about.html', {
        'title': 'О сайте',
    })


def settings(request):
    return render(request, 'tickets/settings.html', {
        'title': 'Настройки',
    })


def support(request):
    context = {
        'title': 'Поддержка'
    }
    return render(request, 'tickets/support.html', context=context)


class TestPage(ModelViewSet):
    queryset = TicketsModel.objects.all()
    serializer_class = TicketsSerializer


class RegisterUser(DataMixin, CreateView):
    form_class = RegisteUserForm
    template_name = 'tickets/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('tickets')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'tickets/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')