from django import forms
from .models import AnswerQuiz


class QuizForm(forms.ModelForm):
    class Meta:
        model=AnswerQuiz
        fields = ['uAnswer']