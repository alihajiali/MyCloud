from django.urls import path
from .views import *

app_name = "account"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("register/", Register.as_view(), name="register"),
    path("login/", Login.as_view(), name="login"),
    path("log_out/", LogOut.as_view(), name="log_out"),
]