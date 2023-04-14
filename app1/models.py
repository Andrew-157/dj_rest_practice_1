from django.db import models


class Product(models.Model):
    TOYS = 'Toys'
    FURNITURE = 'Furniture'
    ELECTRONICS = 'Electronics'
    HOUSEHOLD = 'Household'
    VEHICLE = 'Vehicle'
    PRODUCT_CATEGORIES = [
        (TOYS, 'Toys'),
        (FURNITURE, 'Furniture'),
        (ELECTRONICS, 'Electronics'),
        (HOUSEHOLD, 'Household'),
        (VEHICLE, 'Vehicle')
    ]
    vendor = models.ForeignKey(
        'auth.user', related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    category = models.CharField(choices=PRODUCT_CATEGORIES, max_length=50)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
