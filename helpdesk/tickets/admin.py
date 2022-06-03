from django.contrib import admin
from .models import Tickets, TicketsMessage


class TicketsAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_for_user', 'title', 'status', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('id', 'title', 'status', 'created_at')
    list_editable = ('status',)
    prepopulated_fields = {'slug': ('id_for_user',)}


class TicketsMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'which_ticket', 'content', 'updated_at', 'updated_by', 'created_at')
    list_display_links = ('id', 'content')
    search_fields = ('content',)


admin.site.register(Tickets, TicketsAdmin)
admin.site.register(TicketsMessage, TicketsMessageAdmin)