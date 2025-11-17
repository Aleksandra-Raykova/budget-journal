from django.urls import path
from journal import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'), # dashboard page
    path('reports/', views.reports, name='reports'), # reports page
]
