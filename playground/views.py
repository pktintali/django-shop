from django.shortcuts import render
from django.db import transaction
from django.contrib.contenttypes.models import ContentType
from store.models import Collection, Order, OrderItem, Product
from tags.models import TaggedItem


def say_hello(request):
    queryset = Product.objects.raw(
        'SELECT * FROM store_product'
    )

    return render(
        request, "hello.html", {"name": "Pradeep Kumar","result":list(queryset)}
    )
