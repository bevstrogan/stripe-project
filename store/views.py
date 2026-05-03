import os

import stripe
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from store.models import Item

stripe.api_key = os.getenv("STRIPE_API_KEY")

def buy(request, pk):
    item = get_object_or_404(Item, pk=pk)
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': item.currency,
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price * 100,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url="http://127.0.0.1:8000/",
            cancel_url="http://127.0.0.1:8000/",
        )
        return JsonResponse({'sessionId': session.id})
    except Exception as e:
        return JsonResponse({'error': str(e)})


def items_list(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'store/items_list.html', context)


def items_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {'item': item}
    return render(request, 'store/items_detail.html', context)