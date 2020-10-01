from django.views.generic import FormView, TemplateView, DetailView
from ipware import get_client_ip
from mainapp.forms import QuizForm
from mainapp.models import Quiz, Question, Answer


class IndexView(TemplateView):
    template_name = 'index.html'
    active_quizzes = Quiz.objects.filter(active=True)
    extra_context = {'active_quizzes': active_quizzes}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.user.id
        ip, is_routable = get_client_ip(self.request)
        if self.request.user.is_authenticated:
            user_passed_quizzes = Quiz.objects.filter(question__answer__user_id=user_id).distinct()
        else:
            user_passed_quizzes = Quiz.objects.filter(question__answer__user_ip=ip).distinct()
        context['user_passed_quizzes'] = user_passed_quizzes
        return context


class QuizView(FormView):
    form_class = QuizForm
    template_name = 'start_quiz.html'
    success_url = '/'

    def get_form_kwargs(self):
        user = self.request.user
        pk = self.kwargs.get('pk', None)
        ip, is_routable = get_client_ip(self.request)
        form_kwargs = super(QuizView, self).get_form_kwargs()
        form_kwargs['user'] = user
        form_kwargs['quiz_pk'] = pk
        form_kwargs['ip'] = ip
        return form_kwargs

    def form_valid(self, form):
        form.save()
        return super(QuizView, self).form_valid(form)


class PassedQuizzesView(DetailView):
    model = Quiz
    template_name = 'passed_quizzes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quiz_pk = self.kwargs.get('pk')
        quiz_questions = Question.objects.filter(from_quiz_id=quiz_pk)
        quiz_answers = Answer.objects.filter(answered_question__from_quiz_id=quiz_pk)
        context['quiz_questions'] = quiz_questions
        context['quiz_answers'] = quiz_answers
        return context