from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db import models
from django.utils import timezone
class CustomUserManage(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("Email is must be required!")
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.save()
        return user
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        return self.create_user(email,password,**extra_fields)
class CustomUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=100,blank=False,null=False)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=16)
    is_staff = models.BooleanField(default=True)
    is_supperuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    objects = CustomUserManage()
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']
    def __str__(self):
        return self.name
    