from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render, redirect

from .models import Task, AnswerQuiz, Work
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

def results(request: HttpRequest):
    if request.user.is_authenticated:
        answs = AnswerQuiz.objects.filter(userN=request.user.id, isSubmitted=True)
        if answs:
            all=answs.count()
            count=answs.filter(correct=True).count()
            if count>3:
                if count *2  < all:
                    mark=2
                elif count*4<3*all:
                    mark=3
                elif count*10<all*9:
                    mark=4
                else:mark=5
            else:
                mark=count+2
            context = {
                "all":all,
                "count":count,
                "mark":mark,
                "answs": answs,
                "user": request.user,
            }
        return render(request, "quiz/results.html", context=context)
    else:
        return redirect('myauth:register')


def journal(request: HttpRequest):
    if request.user.is_authenticated:
        answs = AnswerQuiz.objects.all()
        j=[]
        while answs.exists():
            exUserID=answs.first().userID
            ans=answs.filter(userID=exUserID)
            plusList=[]
            for an in ans:
                if an.correct:
                    plusList.append('+')
                else:
                    plusList.append('-')
            u={"name":ans.first().userID.first_name+" "+ans.first().userID.last_name, "plus":plusList,"corAns":plusList.count("+")}
            j.append(u)
            answs=answs.exclude(userID=exUserID)

        context = {
                "tL":j[0]["plus"],
                "uList":j,
                "user": request.user,
        }
        return render(request, "quiz/journal.html", context=context)
    else:
        return redirect('myauth:register')
def work(request:HttpRequest):
    if request.user.is_authenticated:
        if request.method == "POST":
            w = Work.objects.get(pk=1)
            tasks = Task.objects.filter(work=w, toUser=request.user)
            for task in tasks:
                ans=request.POST[str(task.pk)]
                AnswerQuiz.objects.create(
                    uAnswer=ans,
                    correct = ans==str(task.answer),
                    taskID=task,
                    userID=request.user
                )
                task.isSubmitted=True
            w.student.remove(request.user.student)
            return redirect('quiz:res')
        else:
            w=Work.objects.get(pk=1)
            if w.student.filter(user=request.user).exists():
                tasks=Task.objects.filter(work=w,toUser=request.user)
                context ={
                    'w':w,
                    "tasks":tasks,
                    "request":request,
                }
                return render(request, "quiz/work.html", context=context)
            else:
                return redirect('quiz:res') #work done

    else:
        return redirect('myauth:register')

def mainJournal(request: HttpRequest):
    if request.user.is_authenticated:
        answs = AnswerQuiz.objects.all()
        usrs=User.objects.all()
        w=Work.objects.get(pk=1)
        jL=[]
        for usr in usrs:
            ans = answs.filter(userID=usr, taskID__isSubmitted=True)
            plusList = []
            for an in ans:
                if an.correct:
                    plusList.append('+')
                else:
                    plusList.append('-')
            jL.append({"name":usr.first_name+' '+usr.last_name, "pl":plusList,"corAns":plusList.count("+")})

        context = {
            "ans":ans,
            "jL":jL,
            "user": request.user,
        }
        return render(request, "quiz/work_journal.html", context=context)
    else:
        return redirect('myauth:register')
