from django.shortcuts import render

def home(request):
    data = dict()
    data['message'] = 'This is our fantastic project'
    return render(request, 'home.html', context=data)

# Create your views here.
