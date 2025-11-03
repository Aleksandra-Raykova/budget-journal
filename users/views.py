from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth import login
from .forms import CustomUserCreationForm

class RegisterView(FormView):
    template_name = "register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
