from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='homepage'),  # homepage
    path('demo/', views.demo, name='demo'),  # demo journal page
    path('privacy/', views.privacy, name='privacy'),  # privacy page
    path('terms/', views.terms, name='terms'),  # terms page
    path('contact/', views.contact, name='contact'),  # contacts page
]
