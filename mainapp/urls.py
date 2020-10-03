from django.urls import path
from .views import PassedQuizzesView, IndexView, PassedQuizView, ActiveQuizzesView, ActiveQuizView

app_name = 'mainapp'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('active_quizzes/', ActiveQuizzesView.as_view(), name='active_quizzes'),
    path('active_quizzes/<int:pk>', ActiveQuizView.as_view(), name='active_quiz'),
    path('my_quizzes/', PassedQuizzesView.as_view(), name='passed_quizzes'),
    path('my_quizzes/<int:pk>', PassedQuizView.as_view(), name='passed_quiz')
]