from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm, CustomUserLoginForm


class RegisterView(FormView):
    template_name = "register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class ProfileLoginView(FormView):
    template_name = "login.html"
    form_class = CustomUserLoginForm
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


@login_required
def profile(request):
    return render(request, 'profile.html')


class ProfileLogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect("homepage")

