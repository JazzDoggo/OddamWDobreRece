from django.db import models
from users.models import CustomUser


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
    phone_number = models.CharField(max_length=16)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=64)
    pickup_date = models.DateField()
    pickup_time = models.TimeField()
    pickup_comment = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
