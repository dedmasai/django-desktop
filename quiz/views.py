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
                        correct= ans==tObj.answer,
                        userN=request.user.id,
                        isSubmitted=True,
                        taskN=tObj.id,
                        numbInV=tObj.number,
                    )
                    if ans==tObj.answer: tObj.rightAnswCount+=1
                    tObj.isSubmitted=True
                    tObj.save()
                    return redirect('quiz:quiz')
            else:

                form=QuizForm
            context ={
                "t":tObj,
                "form":form,
                "fname":request.user.first_name,
                "lname": request.user.last_name,
            }
        else:
            return redirect('myauth:register')
        return render(request, "quiz/quiz.html", context=context)
    else:
        return redirect('myauth:about-me')
