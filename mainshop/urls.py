from django.urls import path
from mainshop.views import CategoryDetailView, BaseView, CartView, AddToCartView, DeleteFromCartView,ChangeQTYView,CheckOutView,MakeOrderView
from mainshop.views import ProductDetailView

urlpatterns = [
    path("", BaseView.as_view(), name="base"),
    path("products/<str:ct_models>/<str:slug>", ProductDetailView.as_view(), name="product_detail"),
    path("category/<str:slug>/", CategoryDetailView.as_view(), name="category_detail"),
    path("cart/", CartView.as_view(), name="cart"),
    path("add-to-cart/<str:ct_models>/<str:slug>/", AddToCartView.as_view(), name="add_to_cart"),
    path("remove-from-cart/<str:ct_models>/<str:slug>/", DeleteFromCartView.as_view(), name="delete_from_cart"),
    path("change-qty/<str:ct_models>/<str:slug>/", ChangeQTYView.as_view(), name="change_qty"),
    path("checkout/",CheckOutView.as_view(),name= "checkout"),
    path("make-order/",MakeOrderView.as_view(),name= "make_order")

]
