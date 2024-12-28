from django.http import HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404,redirect
from .models import Product,ProductDetail




# Create your views here.
def homepage(request):
    return HttpResponse("<h1>Welcome to my shop!</h1>")

def product_list(request):
    products_data = Product.objects.all()
    products_json = list(products_data.values('id', 'name', 'description', 'price', 'stock', 'created_at'))
    return JsonResponse(products_json,safe=False)


def product(request, pk):
    product = get_object_or_404(Product, pk=pk)  # Fetch the product or return a 404
    product_json = {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": float(product.price),
        "stock": product.stock,
        "created_at": product.created_at,
        "tags": list(product.tags.values("name")),
        "category": {
            "id": product.category.id,
            "name": product.category.name,
            "description": product.category.description,
        },
    }
    return JsonResponse(product_json)

def product_detail(request, pk):
    product_detail = get_object_or_404(ProductDetail, product_id=pk)
    product_detail_json = {
        "id": product_detail.id,
        "manufacturer": product_detail.manufacturer,
        "warranty_period": product_detail.warranty_period,
        "additional_info": product_detail.additional_info
    }
    return JsonResponse(product_detail_json)

def product_redirect_by_slug(request, slug):

    product = get_object_or_404(Product, slug=slug)

    return redirect("product", pk=product.pk)

def product_redirect_by_uuid(request, uuid):

    product = get_object_or_404(Product, uuid=uuid)

    return redirect("product", pk=product.pk)