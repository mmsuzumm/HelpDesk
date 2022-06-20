from rest_framework.serializers import ModelSerializer
from .models import Tickets, TicketsMessage as TicketsMessageModel

class TicketsSerializer(ModelSerializer):

    class Meta:
        model = Tickets
        fields = ['title', 'id_for_user', 'status', 'last_edit_user', 'created_by']
