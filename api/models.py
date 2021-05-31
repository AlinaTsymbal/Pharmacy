from django.contrib.auth.models import User, AbstractUser
from django.db import models


class Pharmacy(models.Model):
    name = models.TextField()
    address = models.TextField()
    phone = models.TextField()

    class Meta:
        db_table = 'pharmacy'


class Category(models.Model):
    name = models.TextField()

    class Meta:
        db_table = 'category'


class RemedySet(models.Model):
    name = models.TextField()
    description = models.TextField()

    class Meta:
        db_table = 'remedy_set'


class MedKit(models.Model):
    name = models.TextField()
    description = models.TextField()

    class Meta:
        db_table = 'med_kit'


class Remedy(models.Model):
    name = models.TextField()
    description = models.TextField(null=True, blank=True)
    categories = models.ManyToManyField(Category, 'remedies', db_table='category_remedy')

    sets = models.ManyToManyField(RemedySet, 'remedies', db_table='remedy_set_remedy')
    med_kits = models.ManyToManyField(MedKit, 'remedies', db_table='med_kit_remedy')

    class Meta:
        db_table = 'remedy'


class PharmacyRemedy(models.Model):
    pharmacy = models.ForeignKey(Pharmacy, models.DO_NOTHING, null=True, blank=True)
    remedy = models.ForeignKey(Remedy, models.DO_NOTHING, null=True, blank=True)
    price = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'pharmacy_remedy'


class AuthUser(AbstractUser):
    type = models.TextField(default='CLIENT')

    class Meta:
        db_table = 'user'


class Client(AuthUser):
    user = models.OneToOneField(AuthUser, models.CASCADE, primary_key=True, related_name='client_data')
    phone = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'client'


class Admin(AuthUser):
    user = models.OneToOneField(AuthUser, models.CASCADE, primary_key=True, related_name='admin_data')

    class Meta:
        db_table = 'admin'


class Basket(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    remedies = models.ManyToManyField(Remedy, 'baskets', db_table='user_basket_remedy')

    class Meta:
        db_table = 'user_basket'
