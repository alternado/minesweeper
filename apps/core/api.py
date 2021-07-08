from django.db import transaction
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.common import constants
from apps.core.models import Username
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

    @action(detail=False, methods=['post'], name='Get or create username')
    def get_or_create(self, request):
        data = request.data
        username = data.get('username')
        username, created = Username.objects.get_or_create(username=username)
        serializer = UsernameSerializer(username, many=False)
        return Response(serializer.data)

