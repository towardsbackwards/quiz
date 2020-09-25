from QuizProject import settings
from coreapp.models import CoreModel, ImageModel
from django.db import models


class Quiz(CoreModel, models.Model):
    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.title


class Question(models.Model):
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
    TYPES = (
        (1, 'One option answer'),
        (2, 'Multiple options answer'),
        (3, 'Text answer'),
    )
    title = models.CharField('Заголовок (должен быть уникальным)', max_length=256, blank=False, null=False, unique=True)
    active = models.BooleanField('Активен ли вопрос', default=True, db_index=True)
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


class AnswerChoice(CoreModel, models.Model):
    class Meta:
        verbose_name = 'Ответ единственным вариантом'
        verbose_name_plural = 'Ответы единственным вариантом'
    user = models.CharField(max_length=2048, verbose_name='ПОльзователь')
    answered_question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, verbose_name='Вопрос')
    single_choice = models.ForeignKey(Choice, on_delete=models.DO_NOTHING, verbose_name='Выбранный вариант')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время ответа')


class AnswersMultiChoice(CoreModel, models.Model):
    class Meta:
        verbose_name = 'Ответ несколькими вариантами'
        verbose_name_plural = 'Ответы несколькими вариантами'
    user = models.CharField(max_length=2048, verbose_name='ПОльзователь')
    answered_question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, verbose_name='Вопрос')
    multi_choice = models.ForeignKey(Choice, on_delete=models.DO_NOTHING, verbose_name='Выбранный вариант')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время ответа')


class AnswerText(CoreModel, models.Model):
    class Meta:
        verbose_name = 'Ответ тектом'
        verbose_name_plural = 'Ответы тектом'
    user = models.CharField(max_length=2048, verbose_name='ПОльзователь')
    answered_question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, verbose_name='Вопрос')
    text_answer = models.ForeignKey(Choice, on_delete=models.DO_NOTHING, verbose_name='Текст ответа')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время ответа')