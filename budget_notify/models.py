from django.db import models
from datetime import datetime


class Shop(models.Model):
    """
    Shops model
    """
    name = models.CharField(max_length=255, db_column='a_name')
    online = models.BooleanField(db_column='a_online')

    class Meta:
        db_table = 't_shops'  # override table name


class Budget(models.Model):
    """
    Budgets Model
    """
    shop_id = models.ForeignKey('Shop', on_delete=models.CASCADE, db_column='a_shop_id')
    month = models.DateTimeField(db_column='a_month')
    budget_amount = models.DecimalField(max_digits=10, decimal_places=2, db_column='a_budget_amount')
    amount_spent = models.DecimalField(max_digits=10, decimal_places=2, db_column='a_amount_spent')

    class Meta:
        db_table = 't_budgets'  # override table name
