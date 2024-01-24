from django.db import models
from user.models import User


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True