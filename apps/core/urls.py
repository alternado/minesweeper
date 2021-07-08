from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.core.api import UsernameApiView
from apps.core.views import IndexView, ChoiceGameView, StartGameView

urlpatterns = []
router = DefaultRouter()
router.register(r'username', UsernameApiView, basename='username')
urlpatterns += [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^choice-game/(?P<username>[-\w]+)/$', ChoiceGameView.as_view(), name='choice_game'),
    url(r'^start-game/(?P<game_board_id>.+)/$', StartGameView.as_view(), name='start_game'),
    url(r'^core/', include((router.urls))),
]
