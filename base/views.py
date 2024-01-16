from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

@login_required(login_url="base:login")
def home(request):
    return render(request, "home.html", {})

# Create your views here.
def authView(request):
   if request.method == "POST":
      form = UserCreationForm(request.POST or None)
      if form.is_valid():
         form.save()
         return redirect("base:login")
   else:
       form = UserCreationForm()
   return render(request, "registration/signup.html", {"form": form})

def sign_out(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("sign_in")
