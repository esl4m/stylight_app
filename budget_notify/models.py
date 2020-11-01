from django.db import models


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
    month = models.CharField(max_length=5, db_column='a_month')
    budget_amount = models.DecimalField(max_digits=10, decimal_places=2, db_column='a_budget_amount')
    amount_spent = models.DecimalField(max_digits=10, decimal_places=2, db_column='a_amount_spent')

    def _get_average_spent(self):
        """
            Returns the average spent.
        """
        return round((self.amount_spent * 100) / self.budget_amount , 2)
    average_spent = property(_get_average_spent)

    class Meta:
        db_table = 't_budgets'  # override table name
