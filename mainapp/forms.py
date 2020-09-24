from django.forms import ModelForm, CharField, Textarea, ModelChoiceField, ModelMultipleChoiceField, \
    CheckboxSelectMultiple

from mainapp.models import Quiz


class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'
        exclude = ('title', 'description', 'active')

    class Media:
        js = ('js/formset.js',)

    def __init__(self, *args, **kwargs):
        self.quiz_pk = kwargs.pop('quiz_pk')
        questions = Quiz.objects.get(id=self.quiz_pk).question_set.all()
        super().__init__(*args, **kwargs)
        for question in questions:
            if question.type == 1:
                self.fields[question.title] = ModelChoiceField(queryset=question.choice_set.all(),
                                                               required=True)
            elif question.type == 2:
                self.fields[question.title] = ModelMultipleChoiceField(widget=CheckboxSelectMultiple,
                                                                       queryset=question.choice_set.all(),
                                                                       required=True)
            elif question.type == 3:
                self.fields[question.title] = CharField(widget=Textarea(),
                                                        label=question.text,
                                                        required=True)
            #self.fields[question.title].widget.attrs['class'] = 'form-control'

    #  при сохранении взять так же пользователя