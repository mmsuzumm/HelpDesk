from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Tickets as TicketsModel, TicketsMessage as TicketsMessageModel
from .forms import *
from django.views.generic import ListView, DetailView, CreateView

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
    model = TicketsModel
    template_name = 'tickets/show_ticket.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.kwargs['slug']
        context['messages'] = TicketsMessageModel.objects.filter(which_ticket=
                                                            self.model.objects.get(slug=self.kwargs['slug']))
        return context


class CreateNewTicket(CreateView):
    form_class = AddTicketForm
    template_name = 'tickets/create_ticket.html'
    success_url = reverse_lazy('tickets')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.form_class)
        print(context)
        return context



# def create_ticket(request):
#     if request.method == 'POST':
#         print(request)
#         form_ticket = AddTicketForm(request.POST)
#         print(form_ticket)
#         form_message = AddTicketsMessageForm(request.POST)
#         print(form_message)
#         if form_ticket.is_valid() and form_message.is_valid():
#             form_message = form_message.cleaned_data
#             form_ticket = form_ticket.cleaned_data
#             form_ticket['slug'] = form_ticket.get('id_for_user')
#             try:
#                 temp_obj = TicketsModel.objects.create(**form_ticket)
#                 form_message['which_ticket'] = temp_obj
#                 TicketsMessageModel.objects.create(**form_message)
#                 return redirect('tickets')
#             except:
#                 form_ticket.add_error(None, 'Ошибка')  # Необходимо вынести в одтельный файл добавление в бд
#     else:
#         form_ticket = AddTicketForm()
#         form_message = AddTicketsMessageForm()
#     context = {
#         'form_ticket': form_ticket,
#         'form_message': form_message,
#     }
#     return render(request, 'tickets/create_ticket.html', context=context)


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


def login(request):
    return HttpResponse('login')


def register(request):
    return HttpResponse('register')

