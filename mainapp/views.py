from django.views.generic import FormView, TemplateView
from ipware import get_client_ip
from mainapp.forms import QuizForm
from mainapp.models import Quiz


class IndexView(TemplateView):
    template_name = 'index.html'
    active_quizzes = Quiz.objects.filter(active=True)
    extra_context = {'active_quizzes': active_quizzes}


class QuizView(FormView):
    form_class = QuizForm
    template_name = 'start_quiz.html'
    success_url = '/'

    def get_form_kwargs(self):
        user = self.request.user
        quiz_pk = self.kwargs.get('quiz_pk', None)
        ip, is_routable = get_client_ip(self.request)
        form_kwargs = super(QuizView, self).get_form_kwargs()
        form_kwargs['user'] = user
        form_kwargs['quiz_pk'] = quiz_pk
        form_kwargs['ip'] = ip
        return form_kwargs

    def form_valid(self, form):
        # if ip not in str(VotersIP.objects.filter(poll_id=poll_id).values('ip')):
        #     store_ip(ip, poll_id)
        # else:
        #     return HttpResponse(f'С данного ip-адреса уже голосовали в этом опросе!')
        form.save()
        return super(QuizView, self).form_valid(form)
