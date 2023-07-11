from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,phone_number,password = None):
        if not email:
            raise ValueError('user must have an email address')

        if not username:
            raise ValueError('user must have an username')
        
        user = self.model(
            email       = self.normalize_email(email),
            username    = username,
            phone_number = phone_number,
            first_name  = first_name,
            last_name   = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,first_name,last_name,username,email,phone_number,password):
        user = self.create_user(
            email       = self.normalize_email(email),
            username    = username,
            phone_number = phone_number,
            password    = password,
            first_name  = first_name,
            last_name   = last_name,
        )
        user.is_admin   = True
        user.is_active  = True
        user.is_staff   = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser,PermissionsMixin):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50,unique=True)
    email           = models.EmailField(max_length=100,unique=True)
    phone_number    = models.CharField(max_length=50)

    # required 
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    
    objects         = MyAccountManager()
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username','phone_number','first_name','last_name']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,add_label):
        return True
