from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from .models import Income, Period
from .forms import IncomeForm
from datetime import date

def get_current_period(user):
    today = date.today()
    period, created = Period.objects.get_or_create(
        user=user,
        year=today.year,
        month=today.month
    )
    return period

@login_required
def income(request):
    current_user = request.user
    current_period = get_current_period(current_user)

    if request.method == "POST":
        form = IncomeForm(request.POST,period=current_period)
        if form.is_valid():
            inc = form.save(commit=False)
            inc.user = current_user
            inc.period = current_period
            inc.save()
            form = IncomeForm()
    else:
        form = IncomeForm()

    incomes = Income.objects.filter(user=current_user, period=current_period)
    total_income = incomes.aggregate(total=Sum('amount'))['total'] or 0

    return render(request, 'incomes.html', {
        'incomes': incomes,
        'form': form,
        'total_income': total_income,
        'period': current_period,
    })

def delete_income(request, pk):
    income_obj = get_object_or_404(Income, pk=pk)

    if request.method == "POST":
        income_obj.delete()
        return redirect('income')

    return HttpResponse(status=405)


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        current_user = self.request.user
        current_period = get_current_period(current_user)

        incomes = Income.objects.filter(user=current_user)
        total_income = incomes.aggregate(total=Sum('amount'))['total'] or 0

        ctx["period"] = current_period
        ctx["incomes"] = incomes
        ctx["total_income"] = total_income

        return ctx


@login_required
def reports(request):
    return render(request, 'reports.html')
