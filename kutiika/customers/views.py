from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, 'customers/login.html')


def register(request):
    return render(request, 'customers/register.html')
