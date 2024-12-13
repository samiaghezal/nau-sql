from django.db import models
from django_prices.models import MoneyField
from django_countries.fields import CountryField
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

from ...core.models import ModelWithMetadata



class DiscountValueTypeEnum(models.TextChoices):
    FIXED = 'FIXED', 'Fixed'
    PERCENTAGE = 'PERCENTAGE', 'Percentage'


class Voucher(ModelWithMetadata):
    type = models.CharField(
        max_length=50,
        choices=VoucherTypeEnum.choices
    )
    name = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=255, unique=True)
    usage_limit = models.IntegerField(null=True, blank=True)
    used = models.IntegerField(default=0)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    apply_once_per_order = models.BooleanField(default=False)
    apply_once_per_customer = models.BooleanField(default=False)
    discount_value_type = models.CharField(
        max_length=50,
        choices=DiscountValueTypeEnum.choices
    )
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    min_spent = MoneyField(
        max_digits=10,
        decimal_places=2,
        currency_field='currency',
        null=True,
        blank=True
    )
    min_checkout_items_quantity = models.IntegerField(null=True, blank=True)
    countries = ArrayField(
        CountryField(),
        default=list,
        blank=True
    )

    class Meta:
        db_table = 'voucher'
        ordering = ['-start_date']
        indexes = [
            models.Index(fields=['code']),
            models.Index(fields=['start_date', 'end_date']),
            models.Index(fields=['type']),
        ]

    def __str__(self):
        return f"{self.code} - {self.name or 'Unnamed Voucher'}"

    @property
    def is_active(self):
        now = timezone.now()
        return (
            self.start_date <= now and
            (not self.end_date or self.end_date >= now) and
            (not self.usage_limit or self.used < self.usage_limit)
        )

    def can_be_used_by_customer(self, customer):
        """Check if voucher can be used by specific customer"""
        if not self.apply_once_per_customer:
            return True
        return not customer.orders.filter(voucher=self).exists()

    def increase_usage(self):
        """Increase the usage counter of the voucher"""
        self.used = models.F('used') + 1
        self.save(update_fields=['used'])

    def calculate_discount(self, base_amount):
        """Calculate discount value based on the voucher type"""
        if self.discount_value_type == DiscountValueTypeEnum.FIXED:
            return min(self.discount_value, base_amount)
        else:  # PERCENTAGE
            return (base_amount * self.discount_value) / 100


class SaleTypeEnum(models.TextChoices):
    PRODUCT_DISCOUNT = 'PRODUCT_DISCOUNT', 'Product Discount'
    ORDER_DISCOUNT = 'ORDER_DISCOUNT', 'Order Discount'
    SHIPPING_DISCOUNT = 'SHIPPING_DISCOUNT', 'Shipping Discount'
    USER_GROUP_DISCOUNT = 'USER_GROUP_DISCOUNT', 'User Group Discount'
    CATEGORY_DISCOUNT = 'CATEGORY_DISCOUNT', 'Category Discount'
    COLLECTION_DISCOUNT = 'COLLECTION_DISCOUNT', 'Collection Discount'
    VARIANT_DISCOUNT = 'VARIANT_DISCOUNT', 'Variant Discount'
    
    


class Sale(ModelWithMetadata):
    name = models.CharField(max_length=255)
    type = models.CharField(
        max_length=50,
        choices=DiscountValueTypeEnum.choices
    )
    sale_type = models.CharField(
        max_length=50,
        choices=SaleTypeEnum.choices
    )
    value = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    min_spent = MoneyField(
        max_digits=10,
        decimal_places=2,
        currency_field='currency',
        null=True,
        blank=True
    )
    min_checkout_items_quantity = models.IntegerField()

    # Related fields
    categories = models.ManyToManyField(
        'product.Category',
        related_name='sales',
        blank=True
    )
    collections = models.ManyToManyField(
        'product.Collection',
        related_name='sales',
        blank=True
    )
    products = models.ManyToManyField(
        'product.Product',
        related_name='sales',
        blank=True
    )
    variants = models.ManyToManyField(
        'product.ProductVariant',
        related_name='sales',
        blank=True
    )
    user_groups = models.ManyToManyField('Group', related_name='sales', blank=True)

    class Meta:
        db_table = 'sale'
        ordering = ['-start_date']
        indexes = [
            models.Index(fields=['start_date', 'end_date']),
            models.Index(fields=['type']),
            models.Index(fields=['sale_type']),
        ]

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"

    @property
    def is_active(self):
        now = timezone.now()
        return (
            self.start_date <= now and
            (not self.end_date or self.end_date >= now)
        )

    def calculate_discount(self, price):
        """Calculate discounted price based on sale type"""
        if not self.is_active:
            return price

        if self.type == DiscountValueTypeEnum.FIXED:
            return max(price - self.value, 0)
        else:  # PERCENTAGE
            discount = (price * self.value) / 100
            return max(price - discount, 0)

    def applies_to_product(self, product):
        """Check if sale applies to a specific product"""
        return (
            self.products.filter(id=product.id).exists() or
            self.categories.filter(id=product.category_id).exists() or
            self.collections.filter(products=product).exists()
        )

    def applies_to_variant(self, variant):
        """Check if sale applies to a specific variant"""
        return (
            self.variants.filter(id=variant.id).exists() or
            self.applies_to_product(variant.product)
        )
