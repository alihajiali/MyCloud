from msilib.schema import Directory
from django.shortcuts import redirect, render
from django.views import View
from .models import *

class CreateDirectory(View):
    def post(self, request):
        data = request.POST
        if data["directory_id"] == '0':
            DirectoryModel.objects.create(user=request.user, name=data["name"])
        else:
            direcory = DirectoryModel.objects.get(id=str(data["directory_id"]))
            DirectoryModel.objects.create(user=request.user, name=data["name"], parent=direcory)
        return redirect("account:home")



class DirectoryView(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user)
            directory = DirectoryModel.objects.filter(user=user).filter(parent=id)
            return render(request, "file/main.html", context={"user": request.user, "directory_id": id, "directory":directory})