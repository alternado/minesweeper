from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from apps.dragamina.api import GameBoardApiView, UsernameGameBoardApiView, ElementGameBoardApiView

router = DefaultRouter()
router.register(r'game-board', GameBoardApiView, basename='game_board')
router.register(r'username-game-board', UsernameGameBoardApiView, basename='username_game_board')
router.register(r'element-game-board', ElementGameBoardApiView, basename='element_game_board')
urlpatterns = router.urls

