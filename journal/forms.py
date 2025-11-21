from django import forms
from .models import Income, Expense, Saving, Investment


class PeriodDateValidationMixin:
    def clean_date(self):
        date = self.cleaned_data.get("date")

        if not date:
            return date

        if date.month != self.period.month or date.year != self.period.year:
            raise forms.ValidationError(
                f"Date must be in {self.period.month_name()} {self.period.year}."
            )

        return date


class OperationAmountValidationMixin:
    def clean(self):
        cleaned = super().clean()
        amount = cleaned.get("amount")
        op = cleaned.get("operation")

        if amount is None or op is None:
            return cleaned

        cleaned["amount"] = amount if op == "add" else -amount
        return cleaned


class IncomeForm(PeriodDateValidationMixin, forms.ModelForm):
    class Meta:
        model = Income
        fields = ("name", "amount", "date")
        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "amount": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
        }

    def __init__(self, *args, period=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.period = period


class ExpenseForm(PeriodDateValidationMixin, forms.ModelForm):
    class Meta:
        model = Expense
        fields = ("name", "amount", "date")
        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "amount": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
        }

    def __init__(self, *args, period=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.period = period


class SavingsForm(PeriodDateValidationMixin, OperationAmountValidationMixin, forms.ModelForm):
    OPERATION_CHOICES = (
        ("add", "Add (+)"),
        ("remove", "Remove (-)"),
    )

    operation = forms.ChoiceField(
        choices=OPERATION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        model = Saving
        fields = ("name", "amount", "date")
        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "amount": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
        }

    def __init__(self, *args, period=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.period = period

    def clean_amount(self):
        amount = self.cleaned_data["amount"]
        if amount < 0:
            raise forms.ValidationError("Amount must be positive.")
        return amount


class InvestmentsForm(PeriodDateValidationMixin, OperationAmountValidationMixin, forms.ModelForm):
    OPERATION_CHOICES = (
        ("add", "Add (+)"),
        ("remove", "Remove (-)"),
    )

    operation = forms.ChoiceField(
        choices=OPERATION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        model = Investment
        fields = ("name", "amount", "date")
        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "amount": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
        }

    def __init__(self, *args, period=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.period = period

    def clean_amount(self):
        amount = self.cleaned_data["amount"]
        if amount < 0:
            raise forms.ValidationError("Amount must be positive.")
        return amount
