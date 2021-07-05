from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'core/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'usuario': False,
        })
        return context


class ChoiceGameView(TemplateView):
    template_name = 'core/choice_game.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'usuario': False,
        })
        return context
