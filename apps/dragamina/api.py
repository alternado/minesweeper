import random

from django.db import transaction
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.common import constants
from apps.core.models import Username
from apps.dragamina.models import GameBoard, UsernameGameBoard, ElementGameBoard
from apps.dragamina.serializers import GameBoardSerializer, UsernameGameBoardSerializer, ElementGameBoardSerializer


class GameBoardApiView(viewsets.ModelViewSet):
    """
    API game board
    """
    serializer_class = GameBoardSerializer

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.all()

    @action(detail=True, methods=['post'], name='Win game board')
    def set_win_game(self, request, pk=None):
        """
        Win game board.

        ---
        parameters:
        - id
        """
        board = self.get_object()
        board.result = constants.RESULT_BOARD_WIN
        board.save()
        serializer = GameBoardSerializer(self.get_object(), many=False)
        return Response(serializer.data)

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
        quantity_mines = 10
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
        mines = ElementGameBoard.objects.filter(game_board=game_board).order_by('?')[:quantity_mines]
        for obj in mines:
            obj.type_element = constants.TYPE_ELEMENT_MINE
            obj.save()

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


class ElementGameBoardApiView(viewsets.ModelViewSet):
    """
    API element game board
    """
    serializer_class = ElementGameBoardSerializer

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.all()

    @action(detail=True, methods=['post'], name='clic element game board')
    def clic_element(self, request, pk=None):
        """
        Clic element game board.

        ---
        parameters:
        - id
        - flag: boolean optional
        """
        element = self.get_object()
        data = request.data
        flag = data.get('flag')
        if element.type_element in (constants.TYPE_ELEMENT_EMPTY, constants.TYPE_ELEMENT_FLAG):
            element.type_element = constants.TYPE_ELEMENT_EMPTY_CLIC
            if flag:
                element.type_element = constants.TYPE_ELEMENT_FLAG
        if element.type_element == constants.TYPE_ELEMENT_MINE:
            element.type_element = constants.TYPE_ELEMENT_MINE_CLIC
            if flag:
                element.type_element = constants.TYPE_ELEMENT_MINE_FLAG
            element.game_board.result = constants.RESULT_BOARD_LOST
            element.game_board.save()
        element.save()

        serializer = ElementGameBoardSerializer(self.get_object(), many=False)
        return Response(serializer.data)
