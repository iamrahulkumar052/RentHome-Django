from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model using AbstractUser
class CustomUser(AbstractUser):
    #make username unique=false and using it to store user's name
    username = models.CharField(max_length=150, unique=False)

    #add role to determine users
    role = models.CharField(max_length=20,default='Renter')

    phone_number = models.CharField(max_length=15, unique=True, null=True)

    #make email=true and using it for login purpose
    email = models.EmailField(unique=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username