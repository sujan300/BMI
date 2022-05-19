from account.models import BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,email,password=None):
        if not email:
            raise ValueError("user must have an email address !")
        user = self.model(
            email           = self.normalize_email(email),
            first_name      = first_name,
            last_name       = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,first_name,last_name,email,password):
        if not email:
            raise ValueError("user must have an email address !")
        user = self.create_user(
            email       = self.normalize_email(email),
            first_name  = first_name,
            last_name   = last_name,
            password    = password,
        )
        user.is_active      =True
        user.is_admin       =True
        user.is_superuser   =True
        user.is_staff       =True
        user.save(using = self._db)
        return user