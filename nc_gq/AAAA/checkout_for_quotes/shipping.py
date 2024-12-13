from django.db import models
from django_measurement.models import MeasurementField
from measurement.measures import Weight
from prices import Money
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator
from prices import MoneyRange
from decimal import Decimal

from ...core.models import ModelWithMetadata


class ShippingMethodTypeEnum(models.TextChoices):
    PRICE = 'PRICE', 'Price Based'
    WEIGHT = 'WEIGHT', 'Weight Based'


class ShippingMethod(ModelWithMetadata):
    name = models.CharField(max_length=255)
    price_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    price_currency = models.CharField(
        max_length=3,
        null=True,
        blank=True
    )
    
    minimum_order_price_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    minimum_order_price_currency = models.CharField(
        max_length=3,
        null=True,
        blank=True
    )
    
    maximum_order_price_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    maximum_order_price_currency = models.CharField(
        max_length=3,
        null=True,
        blank=True
    )
    
    minimum_order_weight = MeasurementField(
        measurement=Weight,
        null=True,
        blank=True
    )
    maximum_order_weight = MeasurementField(
        measurement=Weight,
        null=True,
        blank=True
    )
    
    type = models.CharField(
        max_length=10,
        choices=ShippingMethodTypeEnum.choices,
        default=ShippingMethodTypeEnum.PRICE
    )
    
    requires_secondary_address = models.BooleanField(default=False)

    class Meta:
        db_table = 'shipping_method'
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def price(self) -> Money | None:
        if self.price_amount and self.price_currency:
            return Money(self.price_amount, self.price_currency)
        return None

    @property
    def minimum_order_price(self) -> Money | None:
        if self.minimum_order_price_amount and self.minimum_order_price_currency:
            return Money(
                self.minimum_order_price_amount,
                self.minimum_order_price_currency
            )
        return None

    @property
    def maximum_order_price(self) -> Money | None:
        if self.maximum_order_price_amount and self.maximum_order_price_currency:
            return Money(
                self.maximum_order_price_amount,
                self.maximum_order_price_currency
            )
        return None


class ShippingZoneCountryArea(ModelWithMetadata):
    country_code = models.CharField(max_length=2)
    country_area = models.CharField(max_length=100)
    zone = models.ForeignKey(
        'ShippingZone',
        related_name='country_areas',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'shipping_zone_country_area'
        unique_together = [['zone', 'country_code', 'country_area']]

    def __str__(self):
        return f"{self.zone.name} - {self.country_area}"

    @property
    def country(self) -> dict:
        return {
            'code': self.country_code,
            'name': self.get_country_name()
        }

    def get_country_name(self) -> str:
        # This would typically use django-countries or similar
        # to get the country name from the code
        from django_countries import countries
        return dict(countries).get(self.country_code, self.country_code)


class ShippingZone(ModelWithMetadata):
    name = models.CharField(max_length=255)
    seller = models.ForeignKey(
        'commerce.Seller',
        related_name='shipping_zones',
        on_delete=models.CASCADE
    )
    warehouses = models.ManyToManyField(
        'warehouse.Warehouse',
        related_name='shipping_zones',
        blank=True
    )
    countries = ArrayField(
        models.CharField(max_length=2),
        blank=True,
        default=list
    )
    shipping_methods = models.ManyToManyField(
        ShippingMethod,
        related_name='shipping_zones',
        blank=True
    )
    
    # Price range fields
    price_range_start_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    price_range_start_currency = models.CharField(max_length=3)
    price_range_end_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    price_range_end_currency = models.CharField(max_length=3)

    class Meta:
        db_table = 'shipping_zone'
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def price_range(self) -> MoneyRange:
        start_money = Money(
            self.price_range_start_amount,
            self.price_range_start_currency
        )
        end_money = Money(
            self.price_range_end_amount,
            self.price_range_end_currency
        )
        return MoneyRange(start=start_money, stop=end_money)


class CheckoutSellerShipping(ModelWithMetadata):
    tenant = models.ForeignKey(
        'core.Tenant',
        on_delete=models.CASCADE,
        related_name='checkout_seller_shippings'
    )
    seller = models.ForeignKey(
        'commerce.Seller',
        on_delete=models.CASCADE,
        related_name='checkout_shippings'
    )
    shipping_method = models.ForeignKey(
        ShippingMethod,
        on_delete=models.CASCADE,
        related_name='checkout_seller_shippings'
    )
    is_price_overridden = models.BooleanField(default=False)
    price_override_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00')
    )

    class Meta:
        db_table = 'checkout_seller_shipping'
        unique_together = [['tenant', 'seller']]

    def __str__(self):
        return f"{self.seller.name} - {self.shipping_method.name}"

    @property
    def final_price(self) -> Money:
        if self.is_price_overridden:
            return Money(self.price_override_amount, self.shipping_method.price_currency)
        return self.shipping_method.price
