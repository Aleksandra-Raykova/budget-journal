from django.urls import path
from .views import RegisterView, profile, ProfileLoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', ProfileLoginView.as_view(), name='login' ),
    path('profile/', profile, name='profile'),
]