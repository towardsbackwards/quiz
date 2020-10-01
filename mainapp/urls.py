from django.urls import path
from . import views
from .views import QuizView, IndexView, PassedQuizzesView

app_name = 'mainapp'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('quiz/<int:pk>', QuizView.as_view(), name='quiz'),
    path('my_quizzes/<int:pk>', PassedQuizzesView.as_view(), name='passed')
]