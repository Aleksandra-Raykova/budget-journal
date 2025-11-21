from django.urls import path
from journal import views

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),  # dashboard page
    path('reports/', views.reports, name='reports'),  # reports page
    path('incomes/', views.income, name='income'),  # income table page
    path('incomes/delete/<int:pk>/', views.delete_income, name='delete_income'), # delete row in income table
    path('expenses/', views.expense, name='expense'),  # expense table page
    path('expenses/delete/<int:pk>/', views.delete_expense, name='delete_expense'),  # delete row in expense table
    path('savings/', views.savings, name='saving'),  # savings table page
    path('savings/delete/<int:pk>/', views.delete_saving, name='delete_saving'),  # delete row in saving table
    path('investments/', views.investments, name='investment'),  # investment table page
    path('investments/delete/<int:pk>/', views.delete_investment, name='delete_investment'),  # delete row in investment table
]
