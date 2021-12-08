from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm


# Create your views here.
def login_customer(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('home')
        else:
            messages.success(request, 'The username or password is incorrect')
            return redirect('login')
    else:
        return render(request, 'customers/login.html', {

        })


def logout_customer(request):
    logout(request)
    messages.success(request, 'You Were Logged Out')
    return redirect('home')


def register_customer(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)  # Extends UserCreationForm
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful"))
            return redirect('home')
    else:
        form = RegisterUserForm()

    return render(request, 'customers/register.html', {
        'form': form,
    })
