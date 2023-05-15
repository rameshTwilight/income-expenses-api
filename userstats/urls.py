from django.urls import path

from .views import ExpenseSummaryStats, IncomeSummaryStats

urlpatterns = [
    path("expense-category-data/", ExpenseSummaryStats.as_view(), name="expense_category_summary"),
    path("income-category-data/", IncomeSummaryStats.as_view(), name="income_summary_stats"),
]
