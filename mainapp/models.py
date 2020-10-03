from django.core.exceptions import ValidationError
from authapp.models import Account
from coreapp.models import CoreModel, ImageModel
from django.db import models

TYPES = (
    (1, 'Один верный ответ'),
    (2, 'Несколько верных ответов'),
    (3, 'Свой ответ (текстом)'),
)


class Quiz(CoreModel, models.Model):
    """Модель опроса"""
    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
        ordering = ('id',)

    def __str__(self):
        return self.title


class Question(models.Model):
    """Модель вопроса"""
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ('id',)

    title = models.CharField('Заголовок (должен быть уникальным)',
                             max_length=256,
                             blank=False,
                             null=False,
                             unique=True)
    active = models.BooleanField('Активен ли вопрос',
                                 default=True,
                                 db_index=True)
    type = models.IntegerField(choices=TYPES,
                               default=1,
                               verbose_name='Тип вопроса')
    text = models.CharField(max_length=2048,
                            null=False,
                            blank=False,
                            verbose_name='Текст вопроса')
    from_quiz = models.ForeignKey(Quiz,
                                  on_delete=models.DO_NOTHING,
                                  verbose_name='Опрос', null=True)

    def __str__(self):
        return self.title


class Choice(CoreModel, models.Model):
    """Модель для храниения вариантов выбора в вопросе.
    Может использоваться для определения правильности ответов
    пользователя"""
    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'
        ordering = ('id',)

    from_question = models.ForeignKey(Question,
                                      on_delete=models.CASCADE,
                                      verbose_name='Вопрос')
    text = models.CharField(max_length=2048,
                            null=False,
                            blank=False,
                            verbose_name='Текст варианта')
    correct = models.BooleanField(default=False,
                                  verbose_name='Вариант верен?')

    def __str__(self):
        return self.title


class Answer(CoreModel, models.Model):
    """Модель ответа"""
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ('id',)

    user_ip = models.CharField(max_length=2048,
                               verbose_name='ip')
    user = models.ForeignKey(Account,
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь',
                             null=True)
    answered_question = models.ForeignKey(Question,
                                          on_delete=models.CASCADE,
                                          verbose_name='Вопрос')
    answer_choice = models.ForeignKey(Choice,
                                      on_delete=models.CASCADE,
                                      verbose_name='Выбранный вариант',
                                      null=True)
    answer_text = models.CharField(max_length=2048,
                                   null=True,
                                   verbose_name='Текстовый ответ')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Время ответа')

    def clean(self):
        #  Проверка, что пользователь не забыл ответить на все вопросы
        super().clean()
        if self.answer_choice is None and self.answer_text is None:
            raise ValidationError('Поля ответов answer_choice и answer_text пусты! '
                                  'Должно быть заполнено хотя бы одно из них')

    def __str__(self):
        return f'{self.answered_question} - {self.answer_choice or ""}{self.answer_text or ""}'
