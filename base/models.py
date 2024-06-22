from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, email, phone, password=None, **extra_fields):
        if not(email and phone):
            raise ValueError('Email or Phone must be provided')
        email = self.normalize_email(email)
        user = self.model(username=username.strip(), email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('ADMIN', 'ADMIN'),
        ('SUPERADMIN', 'SUPERADMIN'),
        ('CUSTOMER', 'CUSTOMER')
    )
    username = None
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    phone_number = models.CharField(max_length=180, unique=True)
    USERNAME_FIELD = ["phone"]

    def is_admin(self):
        return self.user_type == 'ADMIN'

    def is_super_admin(self):
        return self.user_type == 'SUPERADMIN'
    
    def is_customer(self):
        return self.user_type == 'CUSTOMER'
    
    pass
