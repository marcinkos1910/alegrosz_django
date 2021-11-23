from django.urls import path

from product import views

urlpatterns = [
    path('', views.product_list, name="product_list"),
    path('<int:pk>', views.product, name="product"),
    path('create', views.create_product, name="product_create")
]
