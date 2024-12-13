from django.db import models
from django_prices.models import MoneyField

from ...core.models import ModelWithMetadata


class PayoutStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    PROCESSING = 'PROCESSING', 'Processing'
    COMPLETED = 'COMPLETED', 'Completed'
    FAILED = 'FAILED', 'Failed'
    CANCELLED = 'CANCELLED', 'Cancelled'


class VendorPayoutStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    PROCESSING = 'PROCESSING', 'Processing'
    PAID = 'PAID', 'Paid'
    FAILED = 'FAILED', 'Failed'
    CANCELLED = 'CANCELLED', 'Cancelled'


class VendorPayoutEventsEnum(models.TextChoices):
    CREATED = 'CREATED', 'Created'
    PROCESSING = 'PROCESSING', 'Processing'
    COMPLETED = 'COMPLETED', 'Completed'
    FAILED = 'FAILED', 'Failed'
    # Add other event types as needed


class VendorPayout(ModelWithMetadata):
    tenant = models.ForeignKey(
        'core.Tenant',
        on_delete=models.CASCADE,
        related_name='vendor_payouts'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    gateway = models.CharField(max_length=255)
    payout = models.ForeignKey(
        'payment.Payout',
        on_delete=models.CASCADE,
        related_name='vendor_payouts'
    )
    seller = models.ForeignKey(
        'commerce.Seller',
        on_delete=models.SET_NULL,
        null=True,
        related_name='vendor_payouts'
    )
    currency = models.CharField(max_length=3)
    average = models.DecimalField(max_digits=10, decimal_places=2)
    discounts = models.DecimalField(max_digits=10, decimal_places=2)
    net = models.DecimalField(max_digits=10, decimal_places=2)
    shipping = models.DecimalField(max_digits=10, decimal_places=2)
    volume_discounts = models.DecimalField(max_digits=10, decimal_places=2)
    commission = models.DecimalField(max_digits=10, decimal_places=2)
    fee_amount = models.DecimalField(max_digits=10, decimal_places=2)
    fees = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    payout_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payable = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    included = models.BooleanField(default=True)
    status = models.CharField(
        max_length=50,
        choices=VendorPayoutStatus.choices,
        default=VendorPayoutStatus.PENDING
    )
    status_message = models.TextField(null=True, blank=True)
    adjustment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    adjustment = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2)
    refund = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    ledger_version = models.BigIntegerField()
    event_types = ArrayField(
        models.CharField(
            max_length=50,
            choices=VendorPayoutEventsEnum.choices
        ),
        default=list
    )
    commission_money = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    discounts_money = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    net_sales = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    shipping_money = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    subtotal = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    total = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')

    class Meta:
        db_table = 'vendor_payout'
        ordering = ['-created']
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['created']),
            models.Index(fields=['ledger_version']),
        ]

    def __str__(self):
        return f"Payout {self.id} for {self.seller.name if self.seller else 'Unknown Seller'}"

    def calculate_total(self):
        """Calculate total payout amount including adjustments and fees"""
        return (
            self.net_sales +
            self.shipping_money -
            self.commission_money -
            self.fees +
            self.adjustment -
            self.refund
        )

    def update_status(self, status, message=None):
        """Update payout status and optionally add a status message"""
        self.status = status
        if message:
            self.status_message = message
        self.save()



class Payout(ModelWithMetadata):
    tenant = models.ForeignKey(
        'core.Tenant',
        on_delete=models.CASCADE,
        related_name='payouts'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField()
    status = models.CharField(
        max_length=50,
        choices=PayoutStatus.choices,
        default=PayoutStatus.PENDING
    )
    name = models.CharField(max_length=255, null=True, blank=True)
    currency = models.CharField(max_length=3)
    vendors = models.IntegerField(default=0)
    net_sales = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    discounts = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    shipping = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    commission = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    fees = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    refunds = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    adjustments = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    payout_amount = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')

    class Meta:
        db_table = 'payout'
        ordering = ['-created']
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['start_date', 'end_date']),
        ]

    def __str__(self):
        return f"Payout {self.id} - {self.name or 'Unnamed'}"

    def calculate_payout_amount(self):
        """Calculate total payout amount"""
        return (
            self.net_sales -
            self.discounts +
            self.shipping -
            self.commission -
            self.fees -
            self.refunds +
            self.adjustments
        ) 
        
        


class JobStatusEnum(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    PROCESSING = 'PROCESSING', 'Processing'
    SUCCESS = 'SUCCESS', 'Success'
    FAILED = 'FAILED', 'Failed'
    DELETED = 'DELETED', 'Deleted'

        
        
class Invoice(ModelWithMetadata):
    number = models.CharField(max_length=255, unique=True)
    external_url = models.URLField(null=True, blank=True)
    status = models.CharField(
        max_length=50,
        choices=JobStatusEnum.choices,
        default=JobStatusEnum.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    message = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    class Meta:
        db_table = 'invoice'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['number']),
            models.Index(fields=['status']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"Invoice {self.number}"

    @property
    def is_valid(self):
        """Check if invoice is valid"""
        return self.status == JobStatusEnum.SUCCESS

    @property
    def is_editable(self):
        """Check if invoice can be edited"""
        return self.status in [JobStatusEnum.PENDING, JobStatusEnum.FAILED]

    def mark_as_success(self, message=None):
        """Mark invoice as successfully processed"""
        self.status = JobStatusEnum.SUCCESS
        if message:
            self.message = message
        self.save(update_fields=['status', 'message', 'updated_at'])

    def mark_as_failed(self, message=None):
        """Mark invoice as failed"""
        self.status = JobStatusEnum.FAILED
        if message:
            self.message = message
        self.save(update_fields=['status', 'message', 'updated_at'])

    def mark_as_pending(self, message=None):
        """Mark invoice as pending"""
        self.status = JobStatusEnum.PENDING
        if message:
            self.message = message
        self.save(update_fields=['status', 'message', 'updated_at']) 