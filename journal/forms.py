from django import forms
from .models import Income, Expense

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


class IncomeForm(PeriodDateValidationMixin, forms.ModelForm):
    class Meta:
        model = Income
        fields = ("source", "amount", "date")
        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "source": forms.TextInput(attrs={"class": "form-control"}),
            "amount": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
        }

    def __init__(self, *args, period=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.period = period


class ExpenseForm(PeriodDateValidationMixin, forms.ModelForm):
    class Meta:
        model = Expense
        fields = ("bill", "amount", "date")
        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "source": forms.TextInput(attrs={"class": "form-control"}),
            "amount": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
        }

    def __init__(self, *args, period=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.period = period
