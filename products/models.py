from django.db import models

def upload_to(instance, filename):
    return f'products/{filename}'

class Product(models.Model):
    name = models.CharField(verbose_name='Product name', max_length=200, null=False, blank=False)
    stock = models.IntegerField(verbose_name='Stock', null=False, blank=False)
    price = models.DecimalField(verbose_name='Price',max_digits=5, decimal_places=2, null=False, blank=False)
    description = models.TextField(verbose_name='Description', null=False, blank=False)
    category = models.CharField(verbose_name='Category', max_length=200)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)

    class Meta:
        db_table = 'product'
        constraints = [
            models.CheckConstraint(
                name='stock_greater_or_equal_0',
                check=models.Q(stock__gte=0)
            ),
            models.CheckConstraint(
                name='price_greater_than_0',
                check=models.Q(price__gt=0)
            )
        ]


