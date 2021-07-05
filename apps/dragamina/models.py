from django.db import models

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
