from django.http import HttpResponse, JsonResponse
from api import models

# Create your views here.
def index(request):
    http = ''
    our_products = models.Product.objects.filter(is_active=True, quantity__gt=0)
    for product in our_products:
        http += f'{product.name} - {product.price} - {product.quantity}<br>'
    print(our_products)
    return HttpResponse(http)


def prod(request):
    our_products = models.Product.objects.filter(is_active=True, quantity__gt=0)
    product_list = list(our_products.values())
    return JsonResponse(product_list, safe=False)