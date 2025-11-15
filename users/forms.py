from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth import authenticate


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({
            "placeholder": "Email address",
            "class": "form-control"
        })
        self.fields["password1"].widget.attrs.update({
            "placeholder": "Password",
            "class": "form-control"
        })
        self.fields["password2"].widget.attrs.update({
            "placeholder": "Confirm password",
            "class": "form-control"
        })


class CustomUserLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        user = authenticate(username=email, password=password)

        if not user:
            raise forms.ValidationError("Invalid email or password.")

        self.user_cache = user
        return self.cleaned_data

    def get_user(self):
        return self.user_cache

