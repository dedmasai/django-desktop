from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy,reverse
from django.views.generic import TemplateView, CreateView
from .forms import CustomUserForm, MyUserCreationForm

# Create your views here.
class AboutMeView(TemplateView):
        template_name = 'myauth/about-me.html'



class RegisterView(CreateView):
    form_class = MyUserCreationForm
    template_name = 'myauth/register.html'
    success_url = reverse_lazy("myauth:welcome")


def register_page(request):
    if request.method != 'POST':
        form = CustomUserForm()
    else:
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=authenticate(request,username=request.POST["username"],password=request.POST["password"])
            if user is not None:
                login(request,user)
            return redirect(reverse('myauth:welcome'))
    context = {
        'ia': request.user.is_authenticated,
        'form': form
    }
    return render(request, 'myauth/register.html', context)
def welcome(request):
    ia=request.user.is_authenticated
    f=''
    l=''
    if request.user.is_authenticated:
        f=request.user.first_name
        l=request.user.last_name
    context = {'ia': ia,
               'f':f,
               'l':l}
    return render(request, "myauth/index.html",context)

class MyLogoutView(LogoutView):
    next_page = reverse_lazy("myauth:welcome")

def logout_view(request):
    logout(request)
    return redirect('myauth:welcome')