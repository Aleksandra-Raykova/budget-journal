from django.urls import path
from journal import views

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),  # dashboard page
    path('reports/', views.reports, name='reports'),  # reports page
    path('incomes/', views.income, name='income'),  # income table page
    path('incomes/delete/<int:pk>/', views.delete_income, name='delete_income'), # delete row in income table
    path('expenses/', views.expense, name='expense'),  # expense table page
    path('expenses/delete/<int:pk>/', views.delete_expense, name='delete_expense'),  # delete row in expense table
]
