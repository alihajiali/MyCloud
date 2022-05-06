from django.urls import path
from .views import *

app_name = "file"

urlpatterns = [
    path("new_directory/", CreateDirectory.as_view(), name="new_directory"),
    path("create_file/", CreateFile.as_view(), name="create_file"),
    path("directory/<int:id>/", DirectoryView.as_view(), name="directory"),

    path("Dmanage/", Delete_item.as_view(), name="delete_manage"),
    path("manage/<str:type>/<int:id>/", Delete_item.as_view(), name="delete_manage"),

    path("Emanage/", Edit_item.as_view(), name="edit_manage"),
    path("manage/<str:type>/<int:id>/", Edit_item.as_view(), name="edit_manage"),

    path("Smanage/", Share_item.as_view(), name="share_manage"), 
    path("manage/<str:type>/<int:id>/", Share_item.as_view(), name="share_manage"),
]