from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

class SpaUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and
        password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

 # create Forfait table
class Forfait(models.Model):
    id  = models.AutoField(primary_key=True)
    price = models.FloatField()
    niche = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    email = models.EmailField()

class SpaUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    niche_number = models.IntegerField(default=0)
    objects = SpaUserManager()
    USERNAME_FIELD = 'email'
    def __str__(self):
        return self.email

  #create search table
class Search(models.Model):
    id = models.AutoField(primary_key=True)
    niche = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    counter = models.IntegerField(default=0)
    user = models.ForeignKey(SpaUser, on_delete=models.CASCADE)


class Payment(models.Model):
        id = models.AutoField(primary_key=True)
        currency = models.CharField(max_length=50)
        isValid = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True)
        user = models.ForeignKey(SpaUser, on_delete=models.CASCADE)
        forfait = models.ForeignKey(Forfait, on_delete=models.CASCADE)

        


