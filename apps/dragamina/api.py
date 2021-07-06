from django.db import transaction
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.common import constants
from apps.core.models import Username
from apps.dragamina.models import GameBoard, UsernameGameBoard, ElementGameBoard
from apps.dragamina.serializers import GameBoardSerializer, UsernameGameBoardSerializer


class GameBoardApiView(viewsets.ModelViewSet):
    """
    API game board
    """
    serializer_class = GameBoardSerializer

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.all()

    @action(detail=False, methods=['post'], name='Create game board')
    def create_board(self, request):
        """
        Create game board by username.

        ---
        parameters:
        - name: username
          required: true
          type: string
        - name: row
          required: true
          type: int
        - name: column
          required: true
          type: int
        """
        rows = 10
        columns = 10
        data = request.data
        # TODO: set unique true username
        username = Username.objects.filter(username=data.get('username')).first()
        # TODO: verify username exists
        # TODO: swagger configuration username input
        game_board = GameBoard.objects.create(
            rows=rows, columns=columns
        )
        for i in range(0, rows):
            for j in range(0, columns):
                ElementGameBoard.objects.create(
                    game_board=game_board, row=i, column=j
                )

        username_game_board = UsernameGameBoard.objects.create(
            username=username, game_board=game_board
        )
        serializer = UsernameGameBoardSerializer(username_game_board, many=False)
        return Response(serializer.data)


class UsernameGameBoardApiView(viewsets.ModelViewSet):
    """
    API username game board
    """
    serializer_class = UsernameGameBoardSerializer

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.all()