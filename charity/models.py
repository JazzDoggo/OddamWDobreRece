from django.contrib.auth.models import User
from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """ Create a new user profile """
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """ Create a new superuser profile """
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system """
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Institution(models.Model):
    fundacja = "1"
    organizacja_pozarzadowa = "2"
    zbiorka_lokalna = "3"
    type_choices = {
        fundacja: "Fundacja",
        organizacja_pozarzadowa: "Organizacja pozarządowa",
        zbiorka_lokalna: "Zbiórka lokalna",
    }

    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=1, choices=type_choices, default=fundacja)
    categories = models.ManyToManyField(Category)

    def get_type(self):
        return self.type_choices[self.type]

    def __str__(self):
        return f'{self.get_type_display()} "{self.name}"'


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.TextField()
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=64)
    pickup_date = models.DateField()
    pickup_time = models.TimeField()
    pickup_comment = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
