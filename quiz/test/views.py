from django.shortcuts import get_object_or_404, get_list_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .forms import TestForm
from .models import Question, Test, Answer, TestCase


class CreateTestView(CreateView):
    form_class = TestForm
    template_name = 'test/create_test.html'
    succes_url = '/success/'

    def form_valid(self, form):
        test = form.save(commit=False)
        test.user = self.request.user
        test.correct_answers = 0
        test.count_of_questions = 20
        test.save()
        return redirect('test:create_test_case', id=test.id)


class CreateTestCaseView(CreateView):
    model = TestCase
    template_name = 'test/create_test_case.html'
    succes_url = '/'
    fields = '__all__'

    def dispatch(self, request, *args, **kwargs):
        self.test = get_object_or_404(Test, pk=kwargs['id'])
        self.question = get_object_or_404(Question, language=self.test.language, pk=2)

        if self.question.type == 'standard':
            self.answers = get_list_or_404(Answer, question=self.question)
            self.count_of_answers = len([answer for answer in self.answers if answer.is_right])

        return super(CreateTestCaseView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(CreateTestCaseView, self).get_context_data(**kwargs)
        ctx['test_id'] = self.test.pk
        ctx['is_last_question'] = 'true' if TestCase.objects.filter(test=self.test).count() == 19 else 'false'
        ctx['question'] = self.question

        if self.question.type == 'standard':
            ctx['answers'] = self.answers
            ctx['count_of_answers'] = self.count_of_answers

        return ctx

    def post(self, request, *args, **kwargs):
        post_args = request.POST

        selected_answer = Answer.objects.get(pk=post_args['selected_answer']) if 'selected_answer' in post_args else None
        free_text = post_args['free_text'] if 'free_text' in post_args else None

        TestCase(
            test=self.test,
            question=self.question,
            selected_answer=selected_answer,
            free_text=free_text
        ).save()

        return redirect('test:create_test_case', id=self.test.pk)


class ShowResultView(DetailView):
    model = Test
    template_name = "test/show_result.html"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        ctx = super(ShowResultView, self).get_context_data(**kwargs)
        ctx['test_case_list'] = TestCase.objects.filter(test_id=self.kwargs['id'])
        return ctx


