from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Shop, Budget


def list_shops(request):
    try:
        shops = Shop.objects.all().order_by('name')
    except Shop.DoesNotExist:
        raise Http404("No Shops")
    return render(request, 'list_shops.html', {'shops': shops})


def get_shop(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    return render(request, 'show_shop.html', {'shop': shop})


def list_budgets(request):
    """
        List all budgets with the average spent
    """
    try:
        budgets = Budget.objects.all().order_by('shop_id')
    except:
        raise Http404("No Budgets")
    return render(request, 'list_budgets.html', {'budgets': budgets})


def check_budget(request):
    """
        Command to scan the budgets and send alerts 
    """
    current_month = datetime.now().month
    budgets = Budget.objects.all().filter(month=current_month)

    if not budgets:
        return HttpResponseNotFound("<h1>No entries for this month</h1>")
    
    for budget in budgets:
        result = {}
        shop = budget.shop_id
        average_spent = (budget.amount_spent * 100) / budget.budget_amount

        if average_spent >= 100 and budget.shop_id.online:
            shop.online = False
            shop.save()
            return HttpResponse("<h1>You reached 100% of your budget, your shop will be offline.</h1>")

        elif 50 <= average_spent < 100:
            shop.online = True
            shop.save()
            return HttpResponse("<h1>You reached 50% or more of your current month budget.</h1>")

        elif average_spent < 50:
            shop.online = True
            shop.save()
        
        else:
            continue
        
        remaining_budget = budget.budget_amount - budget.amount_spent
        result['shop_name'] = budget.shop_id.name
        result['amount_spent'] = budget.amount_spent
        result['remaining_budget'] = str(remaining_budget)

    return render(request, 'check.html', {'result': result})
