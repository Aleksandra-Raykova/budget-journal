from django.urls import path
from journal import views

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),  # dashboard page
    path('reports/', views.reports, name='reports'),  # reports page
    path('incomes/', views.income, name='income'),  # current income table page
    path('incomes/delete/<int:pk>/', views.delete_income, name='delete_income'),  # delete row in income table
    path('incomes/archive/<int:year>/<int:month>/', views.income_archive, name='income_archive'), #income archive
    path('expenses/', views.expense, name='expense'),  # expense table page
    path('expenses/delete/<int:pk>/', views.delete_expense, name='delete_expense'),  # delete row in expense table
    path('expenses/archive/<int:year>/<int:month>/', views.expenses_archive, name='expenses_archive'),  # expenses archive
    path('savings/', views.savings, name='saving'),  # savings table page
    path('savings/delete/<int:pk>/', views.delete_saving, name='delete_saving'),  # delete row in saving table
    path('savings/archive/<int:year>/<int:month>/', views.savings_archive, name='savings_archive'), # savings archive
    path('investments/', views.investments, name='investment'),  # investment table page
    path('investments/delete/<int:pk>/', views.delete_investment, name='delete_investment'),  # delete row in investment table
    path('investments/archive/<int:year>/<int:month>/', views.investments_archive, name='investments_archive'), # investments archive

]
