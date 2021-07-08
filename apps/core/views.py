from django.views.generic import TemplateView

from apps.common import constants


class IndexView(TemplateView):
    template_name = 'core/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'usuario': False,
        })
        return context


# TODO : relocate view
class ChoiceGameView(TemplateView):
    template_name = 'core/choice_game.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'username': self.kwargs.get('username'),
        })
        return context

# TODO : relocate view
class StartGameView(TemplateView):
    template_name = 'core/game.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'username_game_board_id': self.kwargs.get('username_game_board_id'),
            'game_board_id': self.kwargs.get('game_board_id'),
            'TYPE_ELEMENT_MINE': constants.TYPE_ELEMENT_MINE,
            'TYPE_ELEMENT_MINE_CLIC': constants.TYPE_ELEMENT_MINE_CLIC,
            'TYPE_ELEMENT_EMPTY_CLIC': constants.TYPE_ELEMENT_EMPTY_CLIC,
            'TYPE_ELEMENT_FLAG': constants.TYPE_ELEMENT_FLAG,
            'TYPE_ELEMENT_MINE_FLAG': constants.TYPE_ELEMENT_MINE_FLAG,
            'RESULT_BOARD_PENDING': constants.RESULT_BOARD_PENDING,
            'RESULT_BOARD_WIN': constants.RESULT_BOARD_WIN,
            'RESULT_BOARD_LOST': constants.RESULT_BOARD_LOST,
        })
        return context
