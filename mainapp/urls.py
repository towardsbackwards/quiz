from django.urls import path
from . import views
from .views import QuizView, IndexView

app_name = 'mainapp'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('quiz/<int:quiz_pk>', QuizView.as_view()),
]