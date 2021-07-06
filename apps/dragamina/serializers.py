from rest_framework import serializers

from apps.dragamina.models import GameBoard, UsernameGameBoard, ElementGameBoard


class ElementGameBoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = ElementGameBoard
        fields = '__all__'


class GameBoardSerializer(serializers.ModelSerializer):
    elements = ElementGameBoardSerializer(many=True, read_only=True)

    class Meta:
        model = GameBoard
        fields = '__all__'


class UsernameGameBoardSerializer(serializers.ModelSerializer):
    game_board = GameBoardSerializer(many=False, read_only=True)

    class Meta:
        model = UsernameGameBoard
        fields = '__all__'
        depth = 3
