from django.db import models
from django.contrib.auth import get_user_model
from django_prices.models import MoneyField
from django.contrib.postgres.fields import ArrayField
from ...core.models import ModelWithMetadata

User = get_user_model()

class Checkout(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_change = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    billing_address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, related_name='checkout_billing')
    shipping_address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, related_name='checkout_shipping')
    note = models.TextField()
    currency = models.CharField(max_length=3)
    discount = MoneyField(max_digits=10, decimal_places=2, currency_field='currency', null=True)
    discount_name = models.CharField(max_length=255, null=True)
    translated_discount_name = models.CharField(max_length=255, null=True)
    voucher_code = models.CharField(max_length=255, null=True)
    po_numbers = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    email = models.EmailField()
    is_shipping_required = models.BooleanField(default=False)
    token = models.UUIDField(unique=True)
    discount_type = models.CharField(max_length=50, choices=[
        ('FIXED', 'Fixed'),
        ('PERCENTAGE', 'Percentage'),
        # Add other voucher types as needed
    ], null=True)
    shipping_sale_discount = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    marketplace_shipping_method = models.ForeignKey('ShippingMethod', on_delete=models.SET_NULL, null=True)
    
    # Money fields for prices
    shipping_price_net = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    shipping_price_gross = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    subtotal_price_net = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    subtotal_price_gross = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    total_price_net = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    total_price_gross = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    marketplace_shipping_price_net = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    marketplace_shipping_price_gross = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')

    class Meta:
        db_table = 'checkout'


class CheckoutLine(models.Model):
    is_line_price_overridden = models.BooleanField(default=False)
    unit_price_overridden_note = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    variant = models.ForeignKey('ProductVariant', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sale = models.ForeignKey('Sale', on_delete=models.SET_NULL, null=True)
    requires_shipping = models.BooleanField(default=False)
    seller = models.ForeignKey('SellerType', on_delete=models.SET_NULL, null=True)

    # Money fields
    total_price_net = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    total_price_gross = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    discounted_unit_price_net = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    discounted_unit_price_gross = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    original_unit_price_net = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    original_unit_price_gross = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    currency = models.CharField(max_length=3)

    class Meta:
        db_table = 'checkout_line'


class CheckoutTheme(ModelWithMetadata):
    confirmation_url = models.URLField()

    class Meta:
        db_table = 'checkout_theme'

    def __str__(self):
        return f"Checkout Theme {self.id}"
    
    
class OrderSource(models.TextChoices):
    CHECKOUT = 'CHECKOUT', 'checkout'
    DRAFT = 'DRAFT', 'draft'
    QUOTE = 'QUOTE', 'quote'
    MANUAL = 'MANUAL', 'manual'
    EXTERNAL = 'EXTERNAL', 'external'
    
    



class QuoteRequest(ModelWithMetadata):
    
    
    QUOTE_REQUEST_STATE_CHOICES = [
        ('PENDING', 'Pending'),
        ('SUBMITTED', 'Submitted'),
        ('ACCEPTED', 'Accepted'),
        ('DECLINED', 'Declined'),
        ('CANCELLED', 'Cancelled')
    ]
    quote_request_state = models.CharField(max_length=20, choices=QUOTE_REQUEST_STATE_CHOICES)
    
    comment = models.TextField(null=True, blank=True)
    customer = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    store = models.ForeignKey('Store', on_delete=models.SET_NULL, null=True)
    line_items = models.ManyToManyField('order.OrderLine', related_name='quote_requests')
    total_price = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    currency = models.CharField(max_length=3)
    
    cart = models.ForeignKey('Cart', on_delete=models.SET_NULL, null=True)
    business_unit = models.ForeignKey('BusinessUnit', on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey('State', on_delete=models.SET_NULL, null=True)
    
   
    
    class Meta:
        db_table = 'quote_request'


class Comment(models.Model):
    comment = models.TextField(null=True, blank=True)
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    
    class Meta:
        db_table = 'comment'

class Quote(ModelWithMetadata):
    
    key = models.CharField(max_length=256, unique=True)
    version = models.IntegerField()
    quote_request = models.ForeignKey('QuoteRequest', on_delete=models.SET_NULL, null=True)
    staged_quote = models.ForeignKey('StagedQuote', on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    valid_to = models.DateTimeField(null=True)
    seller_comments = models.ManyToManyField('Comment', related_name='seller_comments')
    buyer_comments = models.ManyToManyField('Comment', related_name='buyer_comments')
    store = models.ForeignKey('stores.Vendor', on_delete=models.SET_NULL, null=True)
    
    # Price fields
    total_price = MoneyField(max_digits=10, decimal_places=2, currency_field='currency')
    
    
   
    
    QUOTE_STATE_CHOICES = [
        ('PENDING', 'Pending'),  # Default - Seller submitted, awaiting Buyer reply
        ('DECLINED', 'Declined'),  # Buyer declined the Quote
        ('DECLINED_FOR_RENEGOTIATION', 'Declined For Renegotiation'),  # Buyer declined and requested renegotiation
        ('RENEGOTIATION_ADDRESSED', 'Renegotiation Addressed'),  # Seller created new Quote after renegotiation request
        ('ACCEPTED', 'Accepted'),  # Buyer accepted the Quote
        ('WITHDRAWN', 'Withdrawn'),  # Seller withdrew Quote before acceptance
    ]
    quote_state = models.CharField(max_length=10, choices=QUOTE_STATE_CHOICES)
    
  
    class Meta:
        db_table = 'quote'

        
        
class StagedQuote(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    staged_quote_state = models.CharField(max_length=50)  # Enum field for StagedQuoteState
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    quote_request = models.ForeignKey('QuoteRequest', on_delete=models.SET_NULL, null=True)
    quotation_order = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)
    valid_to = models.DateTimeField(null=True)
    seller_comment = models.TextField(null=True)
    state = models.ForeignKey('State', on_delete=models.SET_NULL, null=True)
    custom_fields = models.JSONField(null=True)  # For CustomFields
    created_by = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    last_modified_by = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'staged_quote'
