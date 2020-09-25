from django.contrib import admin

from .models import Question, Choice, Quiz, AnswerChoice, AnswersMultiChoice, AnswerText


class ChoiceInline(admin.TabularInline):
    model = Choice
    exclude = ('description',)
    extra = 0
    fk_name = 'from_question'


class QuestionAdmin(admin.ModelAdmin):
    inlines = (ChoiceInline, )


class QuestionInline(admin.TabularInline):
    model = Question
    exclude = ('description',)
    extra = 0
    fk_name = 'from_quiz'


class QuizAdmin(admin.ModelAdmin):
    inlines = (QuestionInline, )


admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(AnswerChoice)
admin.site.register(AnswersMultiChoice)
admin.site.register(AnswerText)
