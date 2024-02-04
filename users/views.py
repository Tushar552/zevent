from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Account, Account_more_info
from event.models import Event

# In order to use the custom user model, this should be imported
from django.contrib.auth import get_user_model

User = get_user_model()

# Home
def home(request):
    context = {
        'events': Event.objects.all(),  # Assuming you have an Event model with the required fields
    }

    user = request.user
    context["user"] = user

    # Taking the content from the account-more-info Model by filtering the current user's id (which is always unique)
    more_info = Account_more_info.objects.filter(id=user.id)
    context["more_info"] = more_info

    return render(request, 'home.html', context)


# User Signin
def signin(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")

        # Check if the user is registered
        user = authenticate(email=email, password=password)
        if user is None:
            messages.error(request, "Invalid email or password.")
            return render(request, "login.html")

        login(request, user)
        return redirect("/")

    return render(request, "login.html")

# User Signup
def signup(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        email = request.POST.get("email", "")
        phone_no = request.POST.get("phone_no", "")
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        # Check if the user already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "User already exists. Please login.")
            return redirect("login")  # You need to set up a named URL for your login page

        # Check if the passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, "signup.html")

        # Creating the user and saving it
        user = User.objects.create_user(email=email, password=password)
        user.save()
        login(request, user)

        # If the user enters his/her phone no. while creating an account, then after logging in, it creates the content for that particular user's id
        info = Account_more_info.objects.create(id=request.user.id, phone_no=phone_no, author=request.user)
        info.save()

        return redirect("/")

    return render(request, "signup.html")




@login_required(login_url='login')  # Redirect to the login page if the user is not authenticated
def user_details_page(request):
    # Retrieve user information or perform any other necessary logic
    user = request.user
    more_info = Account_more_info.objects.filter(id=user.id)  # Assuming you have a model named Account_more_info

    context = {
        'user': user,
        'more_info': more_info,
    }

    return render(request, 'user_details_page.html', context)


# User Signout
def signout(request):
    logout(request)
    return redirect("/")
