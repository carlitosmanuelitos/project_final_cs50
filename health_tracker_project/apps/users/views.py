from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request, 'users/profile.html')

def register(request):
    return render(request, 'users/register.html')

def login(request):
    return render(request, 'users/login.html')
