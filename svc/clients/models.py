# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from phonenumber_field.modelfields import PhoneNumberField


# # Create your models here.

# class User(AbstractUser):
#     user_type = (
#         ('Customer', 'Customer'),
#         ('Professional', 'Professional')
#     )
#     number = PhoneNumberField(blank=True)
#     zipcode = models.IntegerField(null=True)
#     usertype = models.CharField(max_length=15, choices=user_type, default="Customer")



# class JobPost(models.Model):
#     taskoverview = models.CharField(max_length=300)
#     address = models.CharField(max_length=300)
#     time = models.IntegerField()
#     addinfo = models.TextField()
#     client = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.taskoverview


# class ChatRecord(models.Model):
#     client = models.ForeignKey(User, on_delete=models.CASCADE)
#     professional = models.ForeignKey(User, on_delete=models.CASCADE, related_name="professional")
#     message = models.CharField(max_length=400)
#     side = models.BooleanField(null=True, blank=True)   #True for consumer, False for professional
#     room_name = models.CharField(max_length=300 )
