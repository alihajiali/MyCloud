from django.urls import path
from .views import *

app_name = "file"

urlpatterns = [
    path("new_directory/", CreateDirectory.as_view(), name="new_directory"),
    path("directory/<int:id>/", DirectoryView.as_view(), name="directory"),
]