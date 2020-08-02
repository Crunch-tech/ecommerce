from django.urls import path, include
from .views import HomeView, SignupView, CartView, CheckoutView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("cart/", CartView.as_view(), name="cart"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("registration/", SignupView.as_view(), name="registration"),
]

