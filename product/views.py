from django.shortcuts import render
from .fake_db.products import FAKE_DB_PRODUCTS

def products_list(request):
    context = dict(
        FAKE_DB_PRODUCTS = FAKE_DB_PRODUCTS,
        page_title = "PRODUCTS"
    )
    return render(request, "product/products.html", context)

def product_detail(request, id):
    result = list(filter(lambda x: (x["id"] == id), FAKE_DB_PRODUCTS))
    if result:
        context = dict(
            product = result[0]
        )
        return render(request, "product/product_detail.html", context)