from django.db import models

from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    def __str__(self):
        return self.title

    @property
    def new_price(self):
        return '%.2f'%(float(self.price)*0.8)

    def get_product_discount(self):
        return '3.5%'