from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def reports(request):
    return render(request, 'reports.html')
