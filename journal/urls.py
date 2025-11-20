from django.urls import path
from journal import views

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),  # dashboard page
    path('reports/', views.reports, name='reports'),  # reports page
    path('incomes/', views.income, name='income'),  # income table page
    path('income/delete/<int:pk>/', views.delete_income, name='delete_income'),
]
