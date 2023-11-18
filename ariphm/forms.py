from django import forms
from .models import quiz, AnswerQuiz
class QuizForm(forms.Form):
    name = forms.CharField()


class QuizItForm(forms.ModelForm):
    class Meta:
        model=AnswerQuiz
        fields = ['uAns']