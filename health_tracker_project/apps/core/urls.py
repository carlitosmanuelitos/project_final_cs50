from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Landing page
    path('dashboard/', views.dashboard, name='dashboard'),
    path('ai_insights/', views.ai_insights, name='ai_insights'),
    # Add other URLs specific to core app
]