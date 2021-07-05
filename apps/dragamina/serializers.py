from rest_framework import serializers

from apps.dragamina.models import GameBoard


class GameBoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = GameBoard
        fields = '__all__'
