from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as _login, logout as _logout
from .models import Task
from .forms import TaskForm, RegistrationForm, LoginForm


# Create your views here.


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': "Главная страница сайта", 'tasks': tasks})


def page(request):
    user = request.user
    tasks = Task.objects.filter(user_id=user.id)
    return render(request, 'main/userPage.html', {'title': "Страница пользователя", 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


@login_required(login_url='login')
def create(request):
    error = ""
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            text = form.cleaned_data["text"]
            user = request.user
            task = Task(title=title, text=text, user=user)
            task.save()
            return redirect("userPage")
        else:
            error = "Форма была неверной"
    form = TaskForm()
    context = {
        "form": form
    }
    return render(request, 'main/create.html', context)


@login_required(login_url='login')
def deleteTask(request):
    Task.objects.filter(id=request.POST.get("id")).delete()
    return page(request)


def login(request):
    if request.user.is_authenticated:
        return redirect('userPage')
    else:
        form = LoginForm()
        if request.method == 'POST':
            password = request.POST.get('password')
            username = request.POST.get('username')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                _login(request, user)
                return redirect("userPage")
        context = {'form': form}
        return render(request, 'main/login.html', context)


@login_required(login_url='login')
def logout(request):
    _logout(request)
    return redirect('login')


def register(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect("login")

        context = {'form': form}
        return render(request, 'main/registration.html', context)