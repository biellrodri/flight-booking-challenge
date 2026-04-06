from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from rest_framework import viewsets

from .models import Customer
from .serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


@login_required
def create_customer(request):
    flight_id = request.GET.get("flight_id")

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        Customer.objects.create(user=request.user, name=name, email=email)

        if flight_id:
            return redirect(f"/booking/{flight_id}/")

        return redirect("flights_list")

    return render(request, "pages/create_customer.html")


def register_user(request):
    """
    Handle user registration.

    Creates a new Django user with username and password.
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        User.objects.create_user(username=username, password=password)

        return redirect("/api-auth/login/")

    return render(request, "pages/register.html")
