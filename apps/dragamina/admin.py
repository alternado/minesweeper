from django.contrib import admin

from .models import GameBoard, ElementGameBoard, UsernameGameBoard

admin.site.register(GameBoard)
admin.site.register(ElementGameBoard)
admin.site.register(UsernameGameBoard)
