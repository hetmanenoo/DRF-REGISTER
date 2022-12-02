from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Register(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.login


# class Email(models.Model):
#     name = models.CharField(max_length=100, db_index=False)
#
#     def __str__(self):
#         return self.name
