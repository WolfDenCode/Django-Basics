from django.urls import path
from . import views

urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("products/",views.product_list,name="product-list"),
    path("products/<int:pk>",views.product,name="product"),
    path("products/<int:pk>/details",views.product_detail,name="product-details"),
    path("products/<slug:slug>", views.product_redirect_by_slug, name="product-redirect-slug"),
    path("products/<uuid:uuid>", views.product_redirect_by_uuid, name="product-redirect-uuid"),
]