from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'core/dashboard.html')

def ai_insights(request):
    return render(request, 'core/ai_insights.html')

def home(request):
    return render(request, 'core/home.html')