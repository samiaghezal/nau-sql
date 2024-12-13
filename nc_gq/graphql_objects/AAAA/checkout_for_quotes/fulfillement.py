from django.db import models
from django_prices.models import MoneyField
from django.contrib.postgres.fields import ArrayField

from ...core.models import ModelWithMetadata


class FulfillmentStatus(models.TextChoices):
    FULFILLED = 'FULFILLED', 'Fulfilled'
    CANCELED = 'CANCELED', 'Canceled'
    REFUNDED = 'REFUNDED', 'Refunded'
    RETURNED = 'RETURNED', 'Returned'
    REPLACED = 'REPLACED', 'Replaced'
    # Add other statuses as needed


class Fulfillment(ModelWithMetadata):
    fulfillment_order = models.IntegerField()
    related_to = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='related_fulfillments'
    )
    order = models.ForeignKey(
        'core.Order',
        on_delete=models.CASCADE,
        related_name='fulfillments'
    )
    nautical_order = models.ForeignKey(
        'core.NauticalOrder',
        on_delete=models.SET_NULL,
        null=True,
        related_name='fulfillments'
    )
    status = models.CharField(
        max_length=50,
        choices=FulfillmentStatus.choices,
        default=FulfillmentStatus.FULFILLED
    )
    tracking_company = models.CharField(max_length=255, null=True, blank=True)
    tracking_number = models.CharField(max_length=255, null=True, blank=True)
    tracking_url = models.URLField(null=True, blank=True)
    shipping_label_url = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        'core.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='fulfillments'
    )
    seller = models.ForeignKey(
        'commerce.Seller',
        on_delete=models.SET_NULL,
        null=True,
        related_name='fulfillments'
    )
    warehouse = models.ForeignKey(
        'warehouse.Warehouse',
        on_delete=models.SET_NULL,
        null=True,
        related_name='fulfillments'
    )
    total_lines_money = MoneyField(
        max_digits=10,
        decimal_places=2,
        currency_field='currency'
    )
    currency = models.CharField(max_length=3)
    custom_fields = ArrayField(
        models.JSONField(),
        default=list,
        blank=True
    )

    class Meta:
        db_table = 'fulfillment'
        ordering = ['fulfillment_order']
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return f"Fulfillment #{self.fulfillment_order} for Order {self.order.number}"

    @property
    def status_display(self):
        return self.status.replace('_', ' ').title()

    @property
    def total_lines_quantity(self):
        return self.lines.aggregate(
            total_quantity=models.Sum('quantity')
        )['total_quantity'] or 0


class FulfillmentLine(ModelWithMetadata):
    fulfillment = models.ForeignKey(
        Fulfillment,
        related_name='lines',
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField()
    order_line = models.ForeignKey(
        'core.OrderLine',
        on_delete=models.SET_NULL,
        null=True,
        related_name='fulfillment_lines'
    )
    return_reason = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'fulfillment_line'

    def __str__(self):
        return f"Fulfillment Line {self.id} - Qty: {self.quantity}"


class FulfillmentReturn(models.Model):
    fulfillment = models.ForeignKey(
        Fulfillment,
        on_delete=models.CASCADE,
        related_name='returns'
    )
    order = models.ForeignKey(
        'core.Order',
        on_delete=models.CASCADE,
        related_name='fulfillment_returns'
    )

    class Meta:
        db_table = 'fulfillment_return'

    def __str__(self):
        return f"Return for Fulfillment #{self.fulfillment.fulfillment_order}"
