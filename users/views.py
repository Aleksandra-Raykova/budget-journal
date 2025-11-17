from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, TemplateView, UpdateView, DeleteView
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm, CustomUserLoginForm
from .models import CustomUser


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


class ProfileLogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect("homepage")


class ProfileDetailView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ["first_name", "last_name", "email"]
    template_name = "edit_profile.html"
    success_url = reverse_lazy("profile")

    def get_object(self, queryset=None):
        return self.request.user


class ProfileDeleteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = request.user
        logout(request)
        user.delete()
        return redirect("homepage")

