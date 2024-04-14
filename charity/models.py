from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)


class Institution(models.Model):
    fundacja = 1
    organizacja_pozarzadowa = 2
    zbiorka_lokalna = 3
    type_choices = {
        fundacja: "Fundacja",
        organizacja_pozarzadowa: "Organizacja pozarządowa",
        zbiorka_lokalna: "Zbiórka lokalna",
    }

    name = models.CharField(max_length=1)
    description = models.TextField()
    type = models.CharField(max_length=64, choices=type_choices, default=fundacja)


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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
