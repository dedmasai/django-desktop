from django.http import HttpRequest
from django.shortcuts import render, redirect

from .models import Task, AnswerQuiz
from .forms import QuizForm

def quiz(request:HttpRequest):
    if request.user.is_authenticated:
        if request.method == "POST":
            form=QuizForm(request.POST)
            if form.is_valid():
                ans=form.cleaned_data["uAnswer"]
                AnswerQuiz.objects.create(uAnswer=ans)
        else:
          #  tsk=
            form=QuizForm
        context ={
            "form":form
        }
    else:
        return redirect('myauth:register')
    return render(request, "quiz/quiz.html", context=context)

# Create your views here.
