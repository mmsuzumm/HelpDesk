from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Tickets


def index(request):
    return render(request, 'tickets/index.html')