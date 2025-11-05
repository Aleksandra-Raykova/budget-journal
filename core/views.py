from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def home(request):
    return render(request, 'homepage.html')


def demo(request):
    return render(request, 'demo.html')


def privacy(request):
    return render(request, 'privacy.html')


def terms(request):
    return render(request, 'terms.html')


def contact(request):
    return render(request, 'contact.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def reports(request):
    return render(request, 'reports.html')

@login_required
def profile(request):
    return render(request, 'profile.html')
