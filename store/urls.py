from django.urls import path, include
from .views import HomeView, SignupView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("registration/", SignupView.as_view(), name="registration"),
]

