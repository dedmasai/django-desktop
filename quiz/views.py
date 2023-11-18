from django.http import HttpRequest
from django.shortcuts import render, redirect

from .models import Task, AnswerQuiz
from .forms import QuizForm


def quiz(request:HttpRequest):
    obj = Task.objects.filter(varNumber=request.user.id, isSubmitted=False)
    if obj:
        tObj=obj[0]
        if request.user.is_authenticated:
            if request.method == "POST":
                form=QuizForm(request.POST)
                if form.is_valid():
                    ans=form.cleaned_data["uAnswer"]
                    AnswerQuiz.objects.create(
                        uAnswer=ans,
                        userN=request.user.id,
                        isSubmitted=True,
                        taskN=tObj.id,
                        numbInV=tObj.number,
                    )
                    tObj.isSubmitted=True
                    tObj.save()
            else:
                form=QuizForm
            context ={
                "t":tObj,
                "form":form
            }
        else:
            return redirect('myauth:register')
        return render(request, "quiz/quiz.html", context=context)
    else:
        return redirect('myauth:welcome')

