from django.db import transaction
from rest_framework import viewsets
from rest_framework.response import Response

from apps.common import constants
from apps.core.serializers import UsernameSerializer
from apps.dragamina.models import GameBoard
from apps.dragamina.serializers import GameBoardSerializer


class UsernameApiView(viewsets.ModelViewSet):
    """
    API username
    """
    serializer_class = UsernameSerializer

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.all()
