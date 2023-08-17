from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from users.models import User
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from products.models import Basket


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect("/")
    else:
        form = UserLoginForm()
    context = {"form": form}
    return render(request, "users/login.html", context)


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "users/registration.html"
    success_url = reverse_lazy("users:login")


@login_required
def profile(request):
    if request.method == "POST":
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("users:profile"))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        "title": "Store - Profile",
        "form": form,
        "baskets": Basket.objects.filter(user=request.user),
    }
    return render(request, "users/profile.html", context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("index"))


