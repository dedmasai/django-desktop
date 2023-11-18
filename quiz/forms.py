from django import forms
from .models import AnswerQuiz


# class QuizForm(forms.Form):
#     class Meta:
#         model=AnswerQuiz
#         fields = ['uAnswer']

class QuizForm(forms.ModelForm):
    class Meta:
        model=AnswerQuiz
        fields = ['uAnswer']
        labels = {
            'uAnswer': 'Введи сюда ответ:'
        }