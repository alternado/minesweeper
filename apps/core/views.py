from django.views.generic import TemplateView


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
        })
        return context
