from django.db import models
from django_prices.models import MoneyField

from ...core.models import ModelWithMetadata


class PriceBookProductHistoryValueType(models.TextChoices):
    FIXED = 'FIXED', 'Fixed'
    PERCENTAGE = 'PERCENTAGE', 'Percentage'


class PriceBook(ModelWithMetadata):
    description = models.TextField()
    description_html = models.TextField()
    name = models.CharField(max_length=255)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'price_book'
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def number_of_products(self):
        return self.price_book_products.count()

    @property
    def number_of_product_types(self):
        return self.price_book_product_types.count()

    @property
    def number_of_variants(self):
        return self.price_book_variants.count()


class PriceBookProductHistory(ModelWithMetadata):
    price_book = models.ForeignKey(
        PriceBook,
        on_delete=models.CASCADE,
        related_name='product_history'
    )
    product_id = models.IntegerField()
    value_type = models.CharField(
        max_length=50,
        choices=PriceBookProductHistoryValueType.choices
    )
    currency = models.CharField(max_length=3)
    created_at = models.DateField(auto_now_add=True)
    price = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    percentage = models.FloatField()
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'price_book_product_history'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['product_id']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"History for Product {self.product_id} in {self.price_book.name}" 