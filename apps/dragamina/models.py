from django.db import models

from apps.common import constants
from apps.common.models import BaseModel
from apps.core.models import Username


class GameBoard(BaseModel):
    rows = models.PositiveSmallIntegerField()
    columns = models.PositiveSmallIntegerField()

    def __str__(self):
        return '{}'.format(self.dimension)

    @property
    def dimension(self):
        return (self.rows * self.columns)


class UsernameGameBoard(BaseModel):
    username = models.ForeignKey(Username, on_delete=models.CASCADE)
    game_board = models.ForeignKey(GameBoard, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.id)


class ElementGameBoard(BaseModel):
    game_board = models.ForeignKey(GameBoard, on_delete=models.CASCADE, related_name='elements')
    row = models.PositiveSmallIntegerField()
    column = models.PositiveSmallIntegerField()
    type_element = models.CharField(max_length=3, choices=constants.TYPE_ELEMENT_BOARD_CHOICES,
                                    default=constants.TYPE_ELEMENT_EMPTY)

    def __str__(self):
        return '{}'.format(self.id)