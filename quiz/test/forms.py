from django import forms

from .models import Test


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('language',)

    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)




