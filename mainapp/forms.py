from django.forms import ModelForm, CharField, Textarea, ModelChoiceField, ModelMultipleChoiceField, \
    CheckboxSelectMultiple, TextInput

from mainapp.models import Quiz


class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'
        exclude = ('title', 'description', 'active')

    def __init__(self, *args, **kwargs):
        self.quiz_pk = kwargs.pop('quiz_pk')
        questions = Quiz.objects.get(id=self.quiz_pk).question_set.all()
        super().__init__(*args, **kwargs)
        for question in questions:
            current = f'{question.title}'
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

    def save(self, commit=True):
        buffer = super(QuizForm, self).save(commit=False)
        print(self.data)

    #  при сохранении взять так же пользователя
