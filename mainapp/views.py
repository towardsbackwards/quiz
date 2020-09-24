from django.views.generic import FormView, TemplateView

from mainapp.forms import QuizForm


class IndexView(TemplateView):
    template_name = 'index.html'


class QuizView(FormView):
    form_class = QuizForm
    template_name = 'start_quiz.html'
    success_url = '/'

    def get_form_kwargs(self):
        quiz_pk = self.kwargs.get('quiz_pk', None)
        form_kwargs = super(QuizView, self).get_form_kwargs()
        form_kwargs['quiz_pk'] = quiz_pk
        return form_kwargs
