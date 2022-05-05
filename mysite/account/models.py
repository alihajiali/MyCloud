from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Account(models.Model):
    TYPE = (
        ("a", "admin"), 
        ("u", "user")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=TYPE, default="u")
    volume = models.BigIntegerField(default=1073741824)
    created_at = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateTimeField(default=datetime.datetime.now() + datetime.timedelta(hours=720))

    def __str__(self):
        return str(self.user)