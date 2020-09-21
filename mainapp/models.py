from coreapp.models import CoreModel, ImageModel
from django.db import models


class QuestionModel(CoreModel, models.Model):
    """Модель участника"""
    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"
    types = (
        ('a', 'Single choice'),
        ('b', 'Multiple choice'),
        ('c', 'Text answer'),
    )
    question_text = models.TextField('Имя участника', max_length=1024)
    question_type = models.CharField(max_length=1, choices=types)

    def __str__(self):
        return f'{self.title}'


class PollEventModel(CoreModel, models.Model):
    """Модель голосования"""
    class Meta:
        verbose_name = "голосование"
        verbose_name_plural = "Голосования"

    date_start = models.DateTimeField(null=True, verbose_name='Дата начала')
    date_end = models.DateTimeField(null=True, verbose_name='Дата завершения')
    question = models.ForeignKey(QuestionModel, verbose_name='Вопрос', on_delete=models.PROTECT)
    votes_limit = models.PositiveIntegerField(null=True, verbose_name='Лимит голосов для досрочного завершения')

    def __str__(self):
        return f'Голосование {self.title}'


# class Votes(CoreModel, models.Model):
#     """Промежуточная модель для хранения данных :голосование - участник - количество голосов:"""
#     class Meta:
#         verbose_name = "Голоса"
#         verbose_name_plural = "Голоса"
#
#     poll = models.ForeignKey(PollEventModel, verbose_name='Голосование', on_delete=models.CASCADE)
#     participant = models.ForeignKey(ParticipantModel, verbose_name='Участники', on_delete=models.CASCADE)
#     participant_votes_count = models.PositiveIntegerField(null=True, verbose_name='Количество голосов', default=0)
#
#     def __str__(self):
#         return f'{self.poll} — {self.participant} (голосов {self.participant_votes_count})'
#
#
# class VotersIP(CoreModel, models.Model):
#     """Модель для хранения данных :опрос - ip голосовавшего:"""
#     poll = models.ForeignKey(PollEventModel, verbose_name='Голосование', on_delete=models.CASCADE)
#     ip = models.GenericIPAddressField()
