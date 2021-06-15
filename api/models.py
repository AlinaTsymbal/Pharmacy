from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.utils import timezone


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
    structure = models.TextField(null=True, blank=True)
    form = models.TextField(null=True, blank=True)
    manufacturer = models.TextField(null=True, blank=True)
    group = models.TextField(null=True, blank=True)
    indication = models.TextField(null=True, blank=True)
    contraindication = models.TextField(null=True, blank=True)
    application_method = models.TextField(null=True, blank=True)
    side_effects = models.TextField(null=True, blank=True)

    sets = models.ManyToManyField(RemedySet, 'remedies', db_table='remedy_set_remedy')
    med_kits = models.ManyToManyField(MedKit, 'remedies', db_table='med_kit_remedy')

    class Meta:
        db_table = 'remedy'


class PharmacyRemedy(models.Model):
    pharmacy = models.ForeignKey(Pharmacy, models.DO_NOTHING, null=True, blank=True)
    remedy = models.ForeignKey(Remedy, models.DO_NOTHING, null=True, blank=True, related_name='pharmacies')
    price = models.TextField(null=True, blank=True)
    is_available = models.BooleanField(default=True)

    class Meta:
        db_table = 'pharmacy_remedy'


class AuthUser(AbstractUser):
    type = models.TextField(default='CLIENT')

    def validate_unique(self, exclude=None):
        pass

    class Meta:
        db_table = 'user'


class Client(models.Model):
    user = models.OneToOneField(AuthUser, models.CASCADE, related_name='client_data', primary_key=True)
    phone = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'client'


class Admin(models.Model):
    user = models.OneToOneField(AuthUser, models.CASCADE, primary_key=True, related_name='admin_data')

    class Meta:
        db_table = 'admin'


class Basket(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_basket'


class BasketRemedy(models.Model):
    remedy = models.ForeignKey(Remedy, on_delete=models.DO_NOTHING)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.DO_NOTHING, null=True, blank=True)
    amount = models.IntegerField(default=1)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='basket_remedies')

    class Meta:
        db_table = 'basket_remedy'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    resolved_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'order'

    @property
    def remedies(self):
        return self.order_remedies


class OrderRemedy(models.Model):
    remedy = models.ForeignKey(Remedy, on_delete=models.DO_NOTHING)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.DO_NOTHING)
    amount = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_remedies')

    class Meta:
        db_table = 'order_remedy'

    @property
    def price(self):
        return self.remedy.pharmacies.get(pharmacy_id=self.pharmacy.id).price

    @property
    def is_available(self):
        return self.remedy.pharmacies.filter(pharmacy_id=self.pharmacy.id).first().is_available
