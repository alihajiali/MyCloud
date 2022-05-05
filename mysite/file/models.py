from django.db import models
from django.contrib.auth.models import User

class DirectoryModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=280)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    size = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class File(models.Model):
    name = models.CharField(max_length=280, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    directory = models.ForeignKey(DirectoryModel, on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(upload_to=f"file/")

    def __str__(self):
        return self.name


class PermissionUser(models.Model):
    TYPE = (
        ("d", "directory"), 
        ("f", "file")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ForeignKey(File, on_delete=models.CASCADE, null=True, blank=True)
    directory = models.ForeignKey(DirectoryModel, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=1, choices=TYPE)

    def __str__(self):
        return self.id