from django.contrib import admin
from .models import *

admin.site.register(DirectoryModel)
admin.site.register(File)
admin.site.register(PermissionUser)