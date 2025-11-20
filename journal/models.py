import calendar

from django.core.validators import MinValueValidator
from django.db import models
from django.conf import settings

# TODO Do I need the Period model or I can filter by date in Income model to work with the tables?
class Period(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    year = models.IntegerField()
    month = models.IntegerField()

    class Meta:
        unique_together = ('user', 'year', 'month')

    def month_name(self):
        return calendar.month_name[self.month]


    def __str__(self):
        return f"{self.month} {self.year}"


class Income(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_incomes")
    period = models.ForeignKey(Period, on_delete=models.CASCADE, related_name="period_incomes")
    source = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0.01)])
    date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source} — {self.amount}"


class Expense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_expenses")
    period = models.ForeignKey(Period, on_delete=models.CASCADE, related_name="period_expenses")
    bill = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0.01)])
    date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bill} — {self.amount}"


class Saving(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_savings")
    period = models.ForeignKey(Period, on_delete=models.CASCADE, related_name="period_savings")
    category = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} — {self.amount}"
