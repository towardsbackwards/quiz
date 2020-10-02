from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import Question, Choice, Quiz, Answer


class ChoiceInline(admin.TabularInline):
    model = Choice
    exclude = ('description',)
    extra = 0
    fk_name = 'from_question'


class QuestionAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js',
            '/static/js/disable_checkbox.js',
        )

    inlines = (ChoiceInline,)


class QuestionInline(admin.TabularInline):

    model = Question
    exclude = ('description',)
    extra = 0
    fk_name = 'from_quiz'


class QuizAdmin(admin.ModelAdmin):
    inlines = (QuestionInline,)


class AnswerAdmin(admin.ModelAdmin):

    readonly_fields = ('answer_choice',
                       'answer_text',
                       'answered_question',
                       'created',
                       'user_ip',
                       'user')
    date_hierarchy = 'created'
    empty_value_display = ''
    list_display = (
        'answered_question',
        'answer_choice',
        'answer_text',
        'get_quiz',
        'created',
        'user_ip',
        'user'
    )

    def get_quiz(self, obj):
        return obj.answered_question.from_quiz

    get_quiz.short_description = 'Название опроса'
    get_quiz.admin_order_field = 'answered_question__from_quiz'

    def get_form(self, request, obj=None, **kwargs):
        if obj.answer_choice is None:
            self.exclude = ('answer_choice', 'title', 'description', 'active')
        elif obj.answer_text is None:
            self.exclude = ('answer_text', 'title', 'description', 'active')
        form = super(AnswerAdmin, self).get_form(request, obj, **kwargs)
        return form


admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Answer, AnswerAdmin)
