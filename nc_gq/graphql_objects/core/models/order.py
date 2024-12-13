from django.db import models
from django_measurement.models import MeasurementField
from measurement.measures import Weight
from django_prices.models import MoneyField, TaxedMoneyField
from django.contrib.postgres.fields import JSONField

from ...core.models import ModelWithMetadata


class OrderOrderSource(models.TextChoices):
    MARKETPLACE = 'MARKETPLACE', 'Marketplace'
    SELLER = 'SELLER', 'Seller'
    EXTERNAL = 'EXTERNAL', 'External'


class OrderStatus(models.TextChoices):
    DRAFT = 'DRAFT', 'Draft'
    UNCONFIRMED = 'UNCONFIRMED', 'Unconfirmed'
    UNFULFILLED = 'UNFULFILLED', 'Unfulfilled'
    PARTIALLY_FULFILLED = 'PARTIALLY_FULFILLED', 'Partially Fulfilled'
    FULFILLED = 'FULFILLED', 'Fulfilled'
    CANCELED = 'CANCELED', 'Canceled'


class OrderSubStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    PROCESSING = 'PROCESSING', 'Processing'
    SHIPPED = 'SHIPPED', 'Shipped'
    # Add other sub-statuses as needed


class PayoutStatusEnum(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    PAID = 'PAID', 'Paid'
    FAILED = 'FAILED', 'Failed'


class OrderEventsEnum(models.TextChoices):
    PLACED = 'PLACED', 'Order Placed'
    CONFIRMED = 'CONFIRMED', 'Order Confirmed'
    FULFILLED = 'FULFILLED', 'Order Fulfilled'
    CANCELLED = 'CANCELLED', 'Order Cancelled'
    # Add other event types as needed


class OrderEventsEmailsEnum(models.TextChoices):
    ORDER_CONFIRMATION = 'ORDER_CONFIRMATION', 'Order Confirmation'
    SHIPPING_CONFIRMATION = 'SHIPPING_CONFIRMATION', 'Shipping Confirmation'
    TRACKING_UPDATED = 'TRACKING_UPDATED', 'Tracking Updated'
    # Add other email types as needed


class SourceFeeEnum(models.TextChoices):
    PAYMENT = 'PAYMENT', 'Payment Fee'
    SHIPPING = 'SHIPPING', 'Shipping Fee'
    # Add other fee sources as needed


class Order(ModelWithMetadata):
    external_id = models.CharField(max_length=255, null=True, blank=True)
    external_source = models.CharField(max_length=255, null=True, blank=True)
    order_source = models.CharField(
        max_length=50,
        choices=OrderOrderSource.choices,
        default=OrderOrderSource.MARKETPLACE
    )
    seller = models.ForeignKey(
        'commerce.Seller',
        on_delete=models.SET_NULL,
        null=True,
        related_name='orders'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=50,
        choices=OrderStatus.choices,
        default=OrderStatus.DRAFT
    )
    sub_status = models.CharField(
        max_length=50,
        choices=OrderSubStatus.choices,
        null=True,
        blank=True
    )
    user = models.ForeignKey(
        'core.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='orders'
    )
    language_code = models.CharField(max_length=10)
    tracking_client_id = models.CharField(max_length=255)
    billing_address = models.ForeignKey(
        'core.Address',
        related_name='order_billing',
        on_delete=models.SET_NULL,
        null=True
    )
    shipping_address = models.ForeignKey(
        'core.Address',
        related_name='order_shipping',
        on_delete=models.SET_NULL,
        null=True
    )
    vat_code = models.CharField(max_length=50)
    eu_invoice_messaging = models.TextField(null=True, blank=True)
    vat_identification_number = models.CharField(max_length=255, null=True, blank=True)
    mp_vat_identification_number = models.CharField(max_length=255, null=True, blank=True)
    currency = models.CharField(max_length=3)
    shipping_method = models.ForeignKey(
        'commerce.ShippingMethod',
        on_delete=models.SET_NULL,
        null=True,
        related_name='orders'
    )
    shipping_method_name = models.CharField(max_length=255, null=True, blank=True)
    shipping_price_net = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    shipping_price_gross = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    is_shipping_price_overridden = models.BooleanField(default=False)
    token = models.CharField(max_length=255, unique=True)
    voucher = models.ForeignKey(
        'discount.Voucher',
        on_delete=models.SET_NULL,
        null=True,
        related_name='orders'
    )
    discount = MoneyField(max_digits=10, decimal_places=2, currency_field='currency', null=True)
    discount_name = models.CharField(max_length=255, null=True, blank=True)
    translated_discount_name = models.CharField(max_length=255, null=True, blank=True)
    display_gross_prices = models.BooleanField(default=True)
    customer_note = models.TextField(default='')
    weight = MeasurementField(measurement=Weight, null=True, blank=True)
    imported_at = models.DateTimeField(null=True, blank=True)
    number = models.CharField(max_length=255, null=True, blank=True)
    marketplace_order_number = models.CharField(max_length=255, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    payment_status = models.CharField(max_length=50)
    total_net = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    total_gross = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    original_total_net = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    original_total_gross = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    subtotal_net = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    subtotal_gross = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    can_finalize = models.BooleanField(default=False)
    user_email = models.EmailField(null=True, blank=True)
    is_shipping_required = models.BooleanField(default=True)
    payout_status = models.CharField(
        max_length=50,
        choices=PayoutStatusEnum.choices,
        null=True,
        blank=True
    )
    available_payout_balance = MoneyField(
        max_digits=10,
        decimal_places=2,
        currency_field='currency',
        null=True
    )
    seller_commission = MoneyField(
        max_digits=10,
        decimal_places=2,
        currency_field='currency',
        null=True
    )
    volume_discount_net = MoneyField(max_digits=10, decimal_places=2, currency_field='currency', null=True)
    volume_discount_gross = MoneyField(max_digits=10, decimal_places=2, currency_field='currency', null=True)
    is_only_seller_on_nautical_order = models.BooleanField(null=True)
    marketplace_order = models.ForeignKey(
        'NauticalOrder',
        on_delete=models.SET_NULL,
        null=True,
        related_name='seller_orders'
    )

    class Meta:
        db_table = 'order'
        ordering = ['-created']
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['created']),
            models.Index(fields=['number']),
            models.Index(fields=['token']),
        ]

    def __str__(self):
        return f"Order {self.number or self.id}"

    @property
    def payment_status_display(self):
        return self.payment_status.replace('_', ' ').title()

    @property
    def status_display(self):
        return self.status.replace('_', ' ').title()


class OrderError(models.Model):
    field = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()
    code = models.CharField(max_length=100)
    warehouse = models.ForeignKey(
        'warehouse.Warehouse',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    order_line = models.ForeignKey(
        'OrderLine',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    variant = models.ForeignKey(
        'product.ProductVariant',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'order_error'


class OrderEvent(ModelWithMetadata):
    date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(
        max_length=50,
        choices=OrderEventsEnum.choices
    )
    user = models.ForeignKey(
        'core.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='order_events'
    )
    message = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    email_type = models.CharField(
        max_length=50,
        choices=OrderEventsEmailsEnum.choices,
        null=True,
        blank=True
    )
    amount = models.FloatField(null=True, blank=True)
    payment_id = models.CharField(max_length=255, null=True, blank=True)
    payment_gateway = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    composed_id = models.CharField(max_length=255, null=True, blank=True)
    order_number = models.CharField(max_length=255, null=True, blank=True)
    invoice_number = models.CharField(max_length=255, null=True, blank=True)
    oversold_items = ArrayField(
        models.CharField(max_length=255),
        null=True,
        blank=True
    )
    warehouse = models.ForeignKey(
        'warehouse.Warehouse',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'order_event'
        ordering = ['-date']


class OrderFee(ModelWithMetadata):
    tenant = models.ForeignKey('core.Tenant', on_delete=models.CASCADE)
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        null=True,
        related_name='fees'
    )
    currency = models.CharField(max_length=3)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_currency = models.CharField(max_length=3)
    transaction_fee = MoneyField(
        max_digits=10,
        decimal_places=2,
        currency_field='transaction_currency',
        null=True
    )
    domiciled_amount = models.DecimalField(max_digits=10, decimal_places=2)
    domiciled_fee = MoneyField(
        max_digits=10,
        decimal_places=2,
        currency_field='currency',
        null=True
    )
    source = models.CharField(
        max_length=50,
        choices=SourceFeeEnum.choices
    )
    name = models.CharField(max_length=255)
    notes = models.TextField()
    data = JSONField(default=dict)

    class Meta:
        db_table = 'order_fee'


class OrderLine(ModelWithMetadata):
    is_line_price_overridden = models.BooleanField(default=False)
    unit_price_overridden_note = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    product_name = models.CharField(max_length=255)
    variant_name = models.CharField(max_length=255)
    product_sku = models.CharField(max_length=255, null=True, blank=True)
    is_shipping_required = models.BooleanField(default=True)
    quantity_fulfilled = models.IntegerField(default=0)
    quantity_declined = models.IntegerField(default=0)
    order = models.ForeignKey(
        Order,
        related_name='lines',
        on_delete=models.CASCADE
    )
    nautical_order_line = models.ForeignKey(
        'NauticalOrderLine',
        on_delete=models.CASCADE
    )
    unit_price_net = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    unit_price_gross = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    total_price_net = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    total_price_gross = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    variant = models.ForeignKey(
        'product.ProductVariant',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    translated_product_name = models.CharField(max_length=255)
    translated_variant_name = models.CharField(max_length=255)
    price_book = models.ForeignKey(
        'commerce.PriceBook',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    quantity_ordered = models.IntegerField()
    unfulfilled_quantity_refunded = models.IntegerField(default=0)
    fulfilled_quantity_refunded = models.IntegerField(default=0)
    currency = models.CharField(max_length=3)

    class Meta:
        db_table = 'order_line'

    def __str__(self):
        return f"{self.product_name} - {self.variant_name}"


class OrderPayoutSummary(models.Model):
    vendor_payout = models.OneToOneField(
        'payment.VendorPayout',
        on_delete=models.CASCADE,
        related_name='summary'
    )
    commissions = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    discounts = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    fees = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    refunds = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    refunds_commission = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    sales = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    shipping = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    total = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    currency = models.CharField(max_length=3)

    class Meta:
        db_table = 'order_payout_summary'


