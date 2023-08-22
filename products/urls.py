from django.urls import path

from products.views import ProductListView, basket_add, basket_remove
from django.views.decorators.cache import cache_page

app_name = "products"

urlpatterns = [
    path("", cache_page(30)(ProductListView.as_view()), name="index"),
    path("category/<int:category_id>/", ProductListView.as_view(), name="category"),  # ../products/category/<category_id>
    path("page/<int:page>/", ProductListView.as_view(), name="paginator"),  # ../products/category/<category_id>
    path("baskets/add/<int:product_id>/", basket_add, name="basket_add"),  # ../products/baskets/add/<product_id>
    path("baskets/remove/<int:basket_id>/", basket_remove, name="basket_remove")  # ../products/baskets/remove/<basket_id>
]
