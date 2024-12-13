from django.db import models
from django_prices.models import MoneyField

class Payment(models.Model):
    gateway = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=255, unique=True)
    checkout = models.ForeignKey('Checkout', on_delete=models.SET_NULL, null=True)
    nautical_order = models.ForeignKey('NauticalOrder', on_delete=models.SET_NULL, null=True)
    payment_method_type = models.CharField(max_length=255)
    payment_method_token = models.CharField(max_length=255, null=True)
    customer_ip_address = models.GenericIPAddressField(null=True)
    charge_status = models.CharField(max_length=50, choices=[
        ('NOT_CHARGED', 'Not charged'),
        ('PARTIALLY_CHARGED', 'Partially charged'),
        ('FULLY_CHARGED', 'Fully charged'),
        ('PARTIALLY_REFUNDED', 'Partially refunded'),
        ('FULLY_REFUNDED', 'Fully refunded')
    ])
    total = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    captured_amount = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    available_capture_amount = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    available_refund_amount = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    currency = models.CharField(max_length=3)

    class Meta:
        db_table = 'payment'

class PaymentMetadata(models.Model):
    payment = models.ForeignKey(Payment, related_name='metadata_items', on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    value = models.TextField()

    class Meta:
        db_table = 'payment_metadata'

class PaymentPrivateMetadata(models.Model):
    payment = models.ForeignKey(Payment, related_name='private_metadata_items', on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    value = models.TextField()

    class Meta:
        db_table = 'payment_private_metadata'

class Transaction(models.Model):
    payment = models.ForeignKey(Payment, related_name='transactions', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=255, unique=True)
    kind = models.CharField(max_length=50)
    is_success = models.BooleanField(default=True)
    error = models.CharField(max_length=255, null=True)
    amount = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    currency = models.CharField(max_length=3)

    class Meta:
        db_table = 'transaction'

class TransactionGatewayResponse(models.Model):
    transaction = models.ForeignKey(Transaction, related_name='gateway_responses', on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    value = models.TextField()

    class Meta:
        db_table = 'transaction_gateway_response'

class CreditCard(models.Model):
    payment = models.OneToOneField(Payment, related_name='credit_card', on_delete=models.CASCADE)
    brand = models.CharField(max_length=50)
    last_digits = models.CharField(max_length=4)
    exp_month = models.IntegerField()
    exp_year = models.IntegerField()

    class Meta:
        db_table = 'credit_card'

class PaymentSource(models.Model):
    gateway_id = models.CharField(max_length=255, primary_key=True)  # Using id from schema as primary key
    gateway = models.CharField(max_length=255)
    credit_card = models.OneToOneField(
        CreditCard,
        on_delete=models.SET_NULL,
        null=True,
        related_name='payment_source'
    )

    class Meta:
        db_table = 'payment_source'

    def __str__(self):
        return f"{self.gateway} - {self.gateway_id}"
