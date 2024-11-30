from inventory.models import Product
from django.db.models import Count, Avg, Max, Min, F
from django.db import connection

def run():

    discount = 0.18
    max_qty_product = Product.objects.annotate(max_qty=Max('qty')).filter(qty=F('max_qty'))
    print(max_qty_product)

    print(connection.queries)

