from django.urls import path
from .views import RegisterView, ProfileLoginView, ProfileLogoutView, ProfileDetailView, ProfileEditView, ProfileDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', ProfileLoginView.as_view(), name='login'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('logout/', ProfileLogoutView.as_view(), name='logout'),
    path('profile/edit/', ProfileEditView.as_view(), name='edit_profile'),
    path('profile/delete/', ProfileDeleteView.as_view(), name='delete_profile'),
]
