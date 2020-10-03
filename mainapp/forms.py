from datetime import datetime

from django.core.exceptions import ValidationError
from django.db.models import Q
from django.forms import ModelForm, CharField, ModelChoiceField, ModelMultipleChoiceField, \
    CheckboxSelectMultiple, TextInput

from mainapp.models import Quiz, Answer, Question


class QuizForm(ModelForm):
    """Универсальная форма опроса"""
    class Meta:
        model = Quiz
        fields = '__all__'
        exclude = ('title', 'description', 'active')

    def __init__(self, *args, **kwargs):
        self.quiz_pk = kwargs.pop('quiz_pk')
        self.ip = kwargs.pop('ip')
        self.user = kwargs.pop('user')
        questions = Quiz.objects.get(id=self.quiz_pk).question_set.all()
        super().__init__(*args, **kwargs)
        for question in questions:
            current = f'{question.title}'
            #  Корректировка отображения полей вопросов в зависимости от их типа
            if question.type == 1:
                self.fields[current] = ModelChoiceField(queryset=question.choice_set.all(),
                                                        required=True)
                self.fields[current].widget.attrs['class'] = 'form-control'
            elif question.type == 2:
                self.fields[current] = ModelMultipleChoiceField(widget=CheckboxSelectMultiple,
                                                                queryset=question.choice_set.all(),
                                                                required=True)
                self.fields[current].widget.attrs['class'] = 'checkbox-inline'
            elif question.type == 3:
                self.fields[current] = CharField(widget=TextInput(),
                                                 label=question.text,
                                                 required=True)
                self.fields[current].widget.attrs['class'] = 'form-control'

    def clean(self):
        """Проверка уникальности пары ip-имя пользователя"""
        cd = self.cleaned_data
        if self.user.is_anonymous:
            # Если пользователь прошел опрос анонимно
            if Answer.objects.filter(Q(user_ip=self.ip) &
                                     Q(answered_question__from_quiz=self.quiz_pk)).exists():
                raise ValidationError("С этого ip уже участвовали в данном опросе")
        else:
            # Если пользователь прошел опрос залогинившись
            if Answer.objects.filter(Q(user_ip=self.ip) &
                                     Q(answered_question__from_quiz=self.quiz_pk) &
                                     Q(user=self.user)).exists():
                raise ValidationError("С этого ip уже участвовали в данном опросе")
        return cd

    def save(self, commit=True):
        # Сохранение моделей ответов в базу в зависимости от
        # тип вопроса, на который был ответ
        now = datetime.now
        for question, answer in self.cleaned_data.items():
            if Question.objects.get(title=question).type == 1:
                Answer.objects.create(user_ip=self.ip,
                                      answered_question=Question.objects.get(title=question),
                                      answer_choice=answer,
                                      created=now,
                                      user=self.user)
            elif Question.objects.get(title=question).type == 2:
                for item in answer:
                    Answer.objects.create(user_ip=self.ip,
                                          answered_question=Question.objects.get(title=question),
                                          answer_choice=item,
                                          created=now,
                                          user=self.user)
            elif Question.objects.get(title=question).type == 3:
                Answer.objects.create(user_ip=self.ip,
                                      answered_question=Question.objects.get(title=question),
                                      answer_text=answer,
                                      created=now,
                                      user=self.user)
