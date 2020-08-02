from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


#  class view for the store page
class HomeView(TemplateView):
    template_name = "store.html"


# class view for checkout page
class CheckoutView(TemplateView):
    template_name = "checkout.html"


#  class view for cart page
class CartView(TemplateView):
    template_name = "cart.html"


class SignupView(CreateView):
    template_name = "registration.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("account")

    def post(self, request):
        form = self.UserCreationForm

        if form.is_valid():
            return HttpResponseRedirect("account")

            return render(request, self.template_name, {"form": form})
