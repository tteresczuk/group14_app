from django.shortcuts import render

def home(request):
    data = dict()
    data['message'] = 'This is our fantastic project'
    return render(request, 'home.html', context=data)

def login(request):
    return render(request, 'login.html')

def new_user_register(request):
    return render(request, 'register.html')

def guest(request):
    return render(request, 'guest.html')

# Create your views here.
