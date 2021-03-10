from django.db import models

from quiz.accounts.models import User

TYPES = (
    ('standard', 'standard'),
    ('free', 'free'),
)


class Language(models.Model):
    name = models.CharField('Язык программирования', max_length=20)

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    def __str__(self):
        return self.name


class Question(models.Model):
    language = models.ForeignKey(Language)
    text = models.TextField('Текст вопроса')
    type = models.CharField('Тип вопроса', choices=TYPES,  max_length=20)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['language']

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.TextField('Текст ответа')
    is_right = models.BooleanField()

    class Meta:
        verbose_name = 'Стандартный ответ'
        verbose_name_plural = 'Стандартные ответы'
        ordering = ['question']

    def __str__(self):
        return self.text


class AnswerFree(models.Model):
    question = models.ForeignKey(Question)
    text = models.TextField('Текст ответа')

    class Meta:
        verbose_name = 'Свобоный ответ'
        verbose_name_plural = 'Свободные ответы'

    def __str__(self):
        return self.text


class Test(models.Model):
    user = models.ForeignKey(User)
    language = models.ForeignKey(Language)
    count_of_questions = models.IntegerField(default=0)
    correct_answers = models.IntegerField()

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
        ordering = ['user']

    def __str__(self):
        return str(self.pk)


class TestCase(models.Model):
    test = models.ForeignKey(Test)
    question = models.ForeignKey(Question)
    selected_answer = models.ForeignKey(Answer, null=True, blank=True)
    free_text = models.TextField('свободный текст', null=True, blank=True)

    class Meta:
        verbose_name = 'Тестовое задание'
        verbose_name_plural = 'Тестовые задания'
        ordering = ['test']

    def __str__(self):
        return str(self.pk)

