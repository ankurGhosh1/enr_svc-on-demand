from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class User(AbstractUser):
    number = PhoneNumberField(null=True)
    zipcode = models.IntegerField(null=True)

    

class JobPost(models.Model):
    taskoverview = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    time = models.IntegerField()
    addinfo = models.TextField()
    client = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.taskoverview