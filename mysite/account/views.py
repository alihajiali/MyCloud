from msilib.schema import Directory
from urllib import request
from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import *
from file.models import *


class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user)
            directory = DirectoryModel.objects.filter(user=user).filter(parent=None)
            return render(request, "file/main.html", context={"user": request.user, "directory_id": 0, "directory":directory})
        else:
            return render(request, 'account/home.html')


class Register(View):
    def get(self, request):
        # return HttpResponse("salam")
        return render(request, "account/register.html")

    def post(self, request):
        data = request.POST
        if data["password"] == data["password_again"] and "@" not in data["username"]:
            User.objects.create(
                username=data["username"], 
                email=data["email"],
                password=data["password"], 
                first_name=data["first_name"],
                last_name=data["last_name"]
            )
            user_ = User.objects.get(username=data["username"])
            Account.objects.create(user=user_)
            login(request, user_)
        return redirect("account:home")


class Login(View):
    def get(self, request):
        return render(request, "account/login.html")
    def post(self, request):
        data=request.POST
        username_or_email=data["username_or_email"]
        if "@" in username_or_email:
            user=User.objects.get(email=username_or_email)
        else:
            user=User.objects.get(username=username_or_email)
        login(request, user)
        return redirect("account:home")



class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect("account:home")