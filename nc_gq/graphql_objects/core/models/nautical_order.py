from django.db import models
from django_measurement.models import MeasurementField
from measurement.measures import Weight
from django_prices.models import MoneyField, TaxedMoneyField

from ...core.models import ModelWithMetadata


class AMOrderOrderSource(models.TextChoices):
    MARKETPLACE = 'MARKETPLACE', 'Marketplace'
    SELLER = 'SELLER', 'Seller'
    EXTERNAL = 'EXTERNAL', 'External'


class AMOrderStatus(models.TextChoices):
    DRAFT = 'DRAFT', 'Draft'
    UNCONFIRMED = 'UNCONFIRMED', 'Unconfirmed'
    UNFULFILLED = 'UNFULFILLED', 'Unfulfilled'
    PARTIALLY_FULFILLED = 'PARTIALLY_FULFILLED', 'Partially Fulfilled'
    FULFILLED = 'FULFILLED', 'Fulfilled'
    CANCELED = 'CANCELED', 'Canceled'


class AMOrderSubStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    PROCESSING = 'PROCESSING', 'Processing'
    SHIPPED = 'SHIPPED', 'Shipped'


class PaymentChargeStatusEnum(models.TextChoices):
    NOT_CHARGED = 'NOT_CHARGED', 'Not Charged'
    PENDING = 'PENDING', 'Pending'
    PARTIALLY_CHARGED = 'PARTIALLY_CHARGED', 'Partially Charged'
    FULLY_CHARGED = 'FULLY_CHARGED', 'Fully Charged'
    PARTIALLY_REFUNDED = 'PARTIALLY_REFUNDED', 'Partially Refunded'
    FULLY_REFUNDED = 'FULLY_REFUNDED', 'Fully Refunded'


class AMOrder(ModelWithMetadata):
    external_id = models.CharField(max_length=255, null=True, blank=True)
    external_source = models.CharField(max_length=255, null=True, blank=True)
    order_source = models.CharField(
        max_length=50,
        choices=AMOrderOrderSource.choices,
        default=AMOrderOrderSource.MARKETPLACE
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=50,
        choices=AMOrderStatus.choices,
        default=AMOrderStatus.DRAFT
    )
    sub_status = models.CharField(
        max_length=50,
        choices=AMOrderSubStatus.choices,
        null=True,
        blank=True
    )
    user = models.ForeignKey(
        'core.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='AM_orders'
    )
    language_code = models.CharField(max_length=10)
    tracking_client_id = models.CharField(max_length=255)
    billing_address = models.ForeignKey(
        'core.Address',
        related_name='AM_orders_billing',
        on_delete=models.SET_NULL,
        null=True
    )
    shipping_address = models.ForeignKey(
        'core.Address',
        related_name='AM_orders_shipping',
        on_delete=models.SET_NULL,
        null=True
    )
    currency = models.CharField(max_length=3)
    is_marketplace_shipping_price_overridden = models.BooleanField(default=False)
    shipping_price_net = MoneyField(max_digits=10, decimal_places=2, currency_field='currency', null=True)
    shipping_price_gross = MoneyField(max_digits=10, decimal_places=2, currency_field='currency', null=True)
    eu_invoice_messaging = models.TextField(null=True, blank=True)
    vat_identification_number = models.CharField(max_length=255, null=True, blank=True)
    mp_vat_identification_number = models.CharField(max_length=255, null=True, blank=True)
    token = models.CharField(max_length=255, unique=True)
    voucher = models.ForeignKey(
        'misc.Voucher',
        on_delete=models.SET_NULL,
        null=True,
        related_name='AM_orders'
    )
    shipping_discount = MoneyField(max_digits=10, decimal_places=2, currency_field='currency', null=True)
    discount = MoneyField(max_digits=10, decimal_places=2, currency_field='currency', null=True)
    discount_name = models.CharField(max_length=255, null=True, blank=True)
    translated_discount_name = models.CharField(max_length=255, null=True, blank=True)
    display_gross_prices = models.BooleanField(default=True)
    customer_note = models.TextField()
    weight = MeasurementField(measurement=Weight, null=True, blank=True)
    imported_at = models.DateTimeField(null=True, blank=True)
    po_numbers = ArrayField(models.CharField(max_length=255), default=list, blank=True)
    number = models.CharField(max_length=255, null=True, blank=True)
    payment_status = models.CharField(
        max_length=50,
        choices=PaymentChargeStatusEnum.choices,
        default=PaymentChargeStatusEnum.NOT_CHARGED
    )
    shipping_method_name = models.CharField(max_length=255)
    marketplace_shipping_price_net = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    marketplace_shipping_price_gross = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    marketplace_shipping_method = models.ForeignKey(
        'shipping.ShippingMethod',
        on_delete=models.SET_NULL,
        null=True,
        related_name='AM_orders'
    )
    marketplace_shipping_method_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'AM_order'
        ordering = ['-created']
        indexes = [
            models.Index(fields=['number']),
            models.Index(fields=['token']),
            models.Index(fields=['status']),
            models.Index(fields=['payment_status']),
        ]

    def __str__(self):
        return f"Order {self.number or self.id}"

    @property
    def is_paid(self):
        return self.payment_status in [
            PaymentChargeStatusEnum.FULLY_CHARGED,
            PaymentChargeStatusEnum.PARTIALLY_CHARGED
        ]

    @property
    def payment_status_display(self):
        return self.get_payment_status_display()

    @property
    def status_display(self):
        return self.get_status_display()

    @property
    def can_finalize(self):
        return self.status == AMOrderStatus.DRAFT

    @property
    def is_shipping_required(self):
        return any(line.is_shipping_required for line in self.lines.all()) 


class AMOrderLine(ModelWithMetadata):
    order = models.ForeignKey(
        AMOrder,
        related_name='lines',
        on_delete=models.CASCADE
    )
    is_line_price_overridden = models.BooleanField(default=False)
    unit_price_overridden_note = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    product_name = models.CharField(max_length=255)
    variant_name = models.CharField(max_length=255)
    product_sku = models.CharField(max_length=255, null=True, blank=True)
    is_shipping_required = models.BooleanField(default=True)
    digital_content_url = models.ForeignKey(
        'product.DigitalContentUrl',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='order_lines'
    )
    size = models.IntegerField(null=True, blank=True)
    unit_price_net = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    unit_price_gross = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    total_price_net = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    total_price_gross = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    variant = models.ForeignKey(
        'product.ProductVariant',
        on_delete=models.SET_NULL,
        null=True,
        related_name='AM_order_lines'
    )
    translated_product_name = models.CharField(max_length=255)
    translated_variant_name = models.CharField(max_length=255)
    price_book = models.ForeignKey(
        'commerce.PriceBook',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='AM_order_lines'
    )
    seller_orderline = models.ForeignKey(
        'core.OrderLine',
        on_delete=models.SET_NULL,
        null=True,
        related_name='AM_order_lines'
    )
    quantity_ordered = models.IntegerField()
    sale = models.ForeignKey(
        'misc.Sale',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='AM_order_lines'
    )
    sale_discount = MoneyField(
        max_digits=10,
        decimal_places=2,
        currency_field='currency',
        null=True,
        blank=True
    )
    voucher_discount = MoneyField(
        max_digits=10,
        decimal_places=2,
        currency_field='currency',
        null=True,
        blank=True
    )
    original_unit_price_net = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    original_unit_price_gross = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    discounted_unit_price_net = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    discounted_unit_price_gross = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    currency = models.CharField(max_length=3)

    class Meta:
        db_table = 'AM_order_line'
        ordering = ['id']
        indexes = [
            models.Index(fields=['product_sku']),
        ]

    def __str__(self):
        return f"{self.product_name} - {self.variant_name} ({self.quantity_ordered})"

    def calculate_total_price(self):
        """Calculate total price based on quantity and unit price"""
        unit_price = self.discounted_unit_price_net if self.discounted_unit_price_net else self.unit_price_net
        return unit_price * self.quantity_ordered

    def apply_sale_discount(self, sale_amount):
        """Apply sale discount to the line"""
        if not self.is_line_price_overridden:
            self.sale_discount = sale_amount
            self.discounted_unit_price_net = self.unit_price_net - sale_amount
            self.discounted_unit_price_gross = self.unit_price_gross - sale_amount
            self.save(update_fields=[
                'sale_discount',
                'discounted_unit_price_net',
                'discounted_unit_price_gross'
            ])

    def apply_voucher_discount(self, voucher_amount):
        """Apply voucher discount to the line"""
        if not self.is_line_price_overridden:
            self.voucher_discount = voucher_amount
            current_net = (
                self.discounted_unit_price_net
                if self.discounted_unit_price_net
                else self.unit_price_net
            )
            current_gross = (
                self.discounted_unit_price_gross
                if self.discounted_unit_price_gross
                else self.unit_price_gross
            )
            self.discounted_unit_price_net = current_net - voucher_amount
            self.discounted_unit_price_gross = current_gross - voucher_amount
            self.save(update_fields=[
                'voucher_discount',
                'discounted_unit_price_net',
                'discounted_unit_price_gross'
            ]) 