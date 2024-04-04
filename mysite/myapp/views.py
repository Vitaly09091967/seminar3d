from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Order

def ordered_items(request):
    # Определение дат для временных интервалов
    end_date = timezone.now()
    start_date_week = end_date - timedelta(days=7)
    start_date_month = end_date - timedelta(days=30)
    start_date_year = end_date - timedelta(days=365)
    
    # Получение уникальных товаров за каждый временной интервал
    items_week = Order.objects.filter(customer=request.user, created_at__range=[start_date_week, end_date]).order_by('product').distinct('product')
    items_month = Order.objects.filter(customer=request.user, created_at__range=[start_date_month, end_date]).order_by('product').distinct('product')
    items_year = Order.objects.filter(customer=request.user, created_at__range=[start_date_year, end_date]).order_by('product').distinct('product')
    
    return render(request, 'ordered_items.html', {'items_week': items_week, 'items_month': items_month, 'items_year': items_year})





# Create your views here.
