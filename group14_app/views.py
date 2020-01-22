from django.shortcuts import render

def home(request):
    data = dict()
    data['message'] = 'This is our fantastic project'
    people = [['John', 'New York', ],
              ['Qing', 'Boston',],
              ['Jill', 'Oslo'],
              ['Raja', 'Stockholm']]
    data['people'] = people
    return render(request, 'home.html', context=data)

def login(request):
    return render(request, 'registration/login.html')

def new_user_register(request):
    return render(request, 'register.html')

def guest(request):
    return render(request, 'guest.html')

def loggedin(request):
    data = dict()
    return render(request,'loggedin.html', context=data)

# Create your views here.
