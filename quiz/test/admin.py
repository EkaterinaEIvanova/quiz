from django.contrib import admin

from quiz.test.models import Test, TestCase, Answer, AnswerFree, Language, Question


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


class AnswerFreeInline(admin.TabularInline):
    model = AnswerFree
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'language',)
    list_filter = ('language', 'type')
    inlines = (AnswerInline, AnswerFreeInline)


class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'language')
    list_filter = ('user', )


class TestCaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'test')
    list_filter = ('test', )


admin.site.register(Test, TestAdmin)
admin.site.register(TestCase)
admin.site.register(Answer)
admin.site.register(AnswerFree)
admin.site.register(Language)
admin.site.register(Question, QuestionAdmin)
