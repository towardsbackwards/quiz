from QuizProject import settings
from coreapp.models import CoreModel, ImageModel
from django.db import models


class Quiz(CoreModel, models.Model):
    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.title


class Question(CoreModel, models.Model):
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
    TYPES = (
        (1, 'One option answer'),
        (2, 'Multiple options answer'),
        (3, 'Text answer'),
    )
    type = models.IntegerField(choices=TYPES, default=1, verbose_name='Тип вопроса')
    text = models.CharField(max_length=2048, null=False, blank=False, verbose_name='Текст вопроса')
    from_quiz = models.ForeignKey(Quiz, on_delete=models.DO_NOTHING, verbose_name='Опрос', null=True)

    def __str__(self):
        return self.title


class Choice(CoreModel, models.Model):
    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'
    from_question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, verbose_name='Вопрос')
    text = models.CharField(max_length=2048, null=False, blank=False, verbose_name='Текст варианта')
    correct = models.BooleanField(default=False, verbose_name='Вариант верен?')

    def __str__(self):
        return self.title



#
#
# class Answer(CoreModel, models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name='ПОльзователь')
#     question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, verbose_name='Вопрос')
#     choice = models.ForeignKey(Choice, on_delete=models.DO_NOTHING, verbose_name='Выбранный вариант')
#     text = models.CharField(max_length=2048, null=False, blank=False, verbose_name='Текст ответа')
#     created = models.DateTimeField(auto_now_add=True, verbose_name='Время ответа')
#
#     def __str__(self):
#         return self.choice.title
