from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import CustomUserForm

# Create your views here.
class AboutMeView(TemplateView):
        template_name = 'myauth/about-me.html'




def register_page(request):
    if request.method != 'POST':
        form = CustomUserForm()
    else:
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myauth:about-me')
    context = {'form': form}

    return render(request, 'myauth/register.html', context)
def welcome(request):
    return render(request, "myauth/welcome.html")