from django.urls import path, include
from . import views


urlpatterns = [
    path('shops/', views.list_shops, name='list-shops'),
    path('shop/<int:pk>/', views.get_shop, name='get-shop'),
    path('budgets/', views.list_budgets, name='list-budgets'),
    path('check/', views.check_budget, name='check-budget'),
]
