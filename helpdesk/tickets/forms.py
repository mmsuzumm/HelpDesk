from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Tickets, TicketsMessage, User


class AddTicketsMessageForm(forms.ModelForm):
    class Meta:
        model = TicketsMessage
        fields = ['content', 'which_ticket']


class AddTicketForm(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ['title', 'id_for_user', 'status', 'created_by']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.TextInput(attrs={'cols': 60, 'rows': 10}),
        }


class AddMessageForm(forms.ModelForm):
    class Meta:
        model = TicketsMessage
        fields = ['content', ]
        widgets = {
            'content': forms.TextInput(attrs={'cols': 60, 'rows': 10, }),
        }

class RegisteUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Придумайте пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'})
        }

