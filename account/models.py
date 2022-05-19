
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from account.myaccountmanager import MyAccountManager

# Create your models here.


class Account(AbstractBaseUser):
    first_name      = models.CharField(max_length=225)
    last_name       = models.CharField(max_length=225)
    age             = models.CharField(max_length=22)
    email           = models.EmailField(max_length=50,unique=True)
    joined_date     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_active       = models.BooleanField(default=False)
    is_admin        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    objects         = MyAccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,add_label):
        return True

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class OtpEmail(models.Model):
    otp = models.IntegerField()
    user= models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.otp)