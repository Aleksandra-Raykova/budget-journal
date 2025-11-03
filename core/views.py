from django.shortcuts import render

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


def dashboard(request):
    return render(request, 'dashboard.html')