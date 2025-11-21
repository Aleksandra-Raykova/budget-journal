from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from .models import Income, Period, Expense, Saving, Investment
from .forms import IncomeForm, ExpenseForm, SavingsForm, InvestmentsForm
from datetime import date


def get_current_period(user):
    today = date.today()
    period, created = Period.objects.get_or_create(
        user=user,
        year=today.year,
        month=today.month
    )
    return period


# TODO - when money are removed from savings and investments there are automatically added to income
@login_required
def income(request):
    current_user = request.user
    current_period = get_current_period(current_user)

    if request.method == "POST":
        form = IncomeForm(request.POST, period=current_period)
        if form.is_valid():
            inc = form.save(commit=False)
            inc.user = current_user
            inc.period = current_period
            inc.save()
            form = IncomeForm(period=current_period)
    else:
        form = IncomeForm(period=current_period)

    all_incomes = Income.objects.filter(user=current_user, period=current_period)
    total_income = all_incomes.aggregate(total=Sum('amount'))['total'] or 0

    return render(request, 'incomes.html', {
        'incomes': all_incomes,
        'form': form,
        'total_income': total_income,
        'period': current_period,
    })


@login_required()
def delete_income(request, pk):
    income_obj = get_object_or_404(Income, pk=pk)

    if request.method == "POST":
        income_obj.delete()
        return redirect('income')

    return HttpResponse(status=405)


@login_required
def expense(request):
    current_user = request.user
    current_period = get_current_period(current_user)

    if request.method == "POST":
        form = ExpenseForm(request.POST, period=current_period)
        if form.is_valid():
            exp = form.save(commit=False)
            exp.user = current_user
            exp.period = current_period
            exp.save()
            form = ExpenseForm(period=current_period)
    else:
        form = ExpenseForm(period=current_period)

    all_expenses = Expense.objects.filter(user=current_user, period=current_period)
    total_expenses = all_expenses.aggregate(total=Sum('amount'))['total'] or 0

    return render(request, 'expenses.html', {
        'expenses': all_expenses,
        'form': form,
        'total_expenses': total_expenses,
        'period': current_period,
    })


@login_required()
def delete_expense(request, pk):
    expense_obj = get_object_or_404(Expense, pk=pk)

    if request.method == "POST":
        expense_obj.delete()
        return redirect('expense')

    return HttpResponse(status=405)


@login_required
def savings(request):
    current_user = request.user
    current_period = get_current_period(current_user)

    if request.method == "POST":
        form = SavingsForm(request.POST, period=current_period)
        if form.is_valid():
            sav = form.save(commit=False)
            sav.user = current_user
            sav.period = current_period
            sav.save()
            form = SavingsForm(period=current_period)
    else:
        form = SavingsForm(period=current_period)

    all_savings = Saving.objects.filter(user=current_user, period=current_period)
    total_savings = all_savings.aggregate(total=Sum('amount'))['total'] or 0

    return render(request, 'savings.html', {
        'savings': all_savings,
        'form': form,
        'total_savings': total_savings,
        'period': current_period,
    })


@login_required()
def delete_saving(request, pk):
    saving_obj = get_object_or_404(Saving, pk=pk)

    if request.method == "POST":
        saving_obj.delete()
        return redirect('saving')

    return HttpResponse(status=405)


@login_required
def investments(request):
    current_user = request.user
    current_period = get_current_period(current_user)

    if request.method == "POST":
        form = InvestmentsForm(request.POST, period=current_period)
        if form.is_valid():
            sav = form.save(commit=False)
            sav.user = current_user
            sav.period = current_period
            sav.save()
            form = InvestmentsForm(period=current_period)
    else:
        form = InvestmentsForm(period=current_period)

    all_investments = Investment.objects.filter(user=current_user, period=current_period)
    total_investments = all_investments.aggregate(total=Sum('amount'))['total'] or 0

    return render(request, 'investments.html', {
        'investments': all_investments,
        'form': form,
        'total_investments': total_investments,
        'period': current_period,
    })


@login_required()
def delete_investment(request, pk):
    investment_obj = get_object_or_404(Investment, pk=pk)

    if request.method == "POST":
        investment_obj.delete()
        return redirect('investment')

    return HttpResponse(status=405)


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        current_user = self.request.user
        current_period = get_current_period(current_user)

        incomes = Income.objects.filter(user=current_user, period=current_period)
        total_income = incomes.aggregate(total=Sum('amount'))['total'] or 0

        expenses = Expense.objects.filter(user=current_user, period=current_period)
        total_expenses = expenses.aggregate(total=Sum('amount'))['total'] or 0

        all_savings = Saving.objects.filter(user=current_user, period=current_period)
        total_savings = all_savings.aggregate(total=Sum('amount'))['total'] or 0

        investments = Investment.objects.filter(user=current_user, period=current_period)
        total_investments = investments.aggregate(total=Sum('amount'))['total'] or 0

        total_remaining = total_income - total_expenses
        total_wealth = total_remaining + total_savings + total_investments

        ctx["period"] = current_period
        ctx["incomes"] = incomes
        ctx["total_income"] = total_income
        ctx["expenses"] = expenses
        ctx["total_expenses"] = total_expenses
        ctx["savings"] = all_savings
        ctx["total_savings"] = total_savings
        ctx["investments"] = investments
        ctx["total_investments"] = total_investments
        ctx["total_remaining"] = total_remaining
        ctx["total_wealth"] = total_wealth

        return ctx


@login_required
def reports(request):
    return render(request, 'reports.html')
