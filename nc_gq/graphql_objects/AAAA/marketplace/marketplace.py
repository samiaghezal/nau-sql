from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid

from ...core.models import WeightUnitsEnum



class CommissionTypeEnum(models.TextChoices):
    MARKETPLACE = 'MARKETPLACE', 'Gross Price Commission'
    WHOLESALE = 'WHOLESALE', 'Markup Commission'
    DROPSHIPPING = 'DROPSHIPPING', 'Absolute Price Commission'



class MarkupCommissionTypeEnum(models.TextChoices):
    PERCENTAGE = 'PERCENTAGE', 'Percentage'
    FIXED = 'FIXED', 'Fixed'
    # Add other markup commission types as needed


class FeeType(models.TextChoices):
    TRANSACTION = 'TRANSACTION', 'Transaction'
    SUBSCRIPTION = 'SUBSCRIPTION', 'Subscription'
    COMBINED = 'COMBINED', 'Combined'
    


class FeeScope(models.TextChoices):
    ORDER = 'ORDER', 'Order'
    PRODUCT = 'PRODUCT', 'Product'
    # Add other fee scopes as needed


class Agreement(ModelWithMetadata):
    publication_date = models.DateField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    content_html = models.TextField()
    tenant = models.ForeignKey(
        'core.Tenant',
        on_delete=models.CASCADE,
        related_name='agreements'
    )
    seo_title = models.CharField(max_length=255, null=True, blank=True)
    seo_description = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    commission_type = models.CharField(
        max_length=50,
        choices=CommissionTypeEnum.choices
    )
    default_commission = models.DecimalField(max_digits=10, decimal_places=2)
    markup_commission_type = models.CharField(
        max_length=50,
        choices=MarkupCommissionTypeEnum.choices
    )
    markup_commission_value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'agreement'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return self.title


class AgreementFees(ModelWithMetadata):
    tenant = models.ForeignKey(
        'core.Tenant',
        on_delete=models.CASCADE,
        related_name='agreement_fees'
    )
    agreement = models.ForeignKey(
        Agreement,
        on_delete=models.CASCADE,
        related_name='fees'
    )
    fee_type = models.CharField(
        max_length=50,
        choices=FeeType.choices
    )
    fee_scope = models.CharField(
        max_length=50,
        choices=FeeScope.choices
    )
    fee_value = models.DecimalField(max_digits=10, decimal_places=2)
    fee_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'agreement_fees'
        verbose_name_plural = 'agreement fees'

    def __str__(self):
        return f"{self.fee_name} - {self.fee_value}"


class AgreementSellers(ModelWithMetadata):
    tenant = models.ForeignKey(
        'core.Tenant',
        on_delete=models.CASCADE,
        related_name='agreement_sellers'
    )
    seller = models.ForeignKey(
        'commerce.Seller',
        on_delete=models.CASCADE,
        related_name='agreements'
    )
    acknowledged_on = models.DateTimeField(null=True, blank=True)
    plan = models.ForeignKey(
        Agreement,
        on_delete=models.SET_NULL,
        null=True,
        related_name='sellers'
    )
    effective_at = models.DateTimeField()

    class Meta:
        db_table = 'agreement_sellers'
        verbose_name_plural = 'agreement sellers'
        unique_together = [['tenant', 'seller', 'plan']]

    def __str__(self):
        return f"{self.seller.name} - {self.plan.title if self.plan else 'No Plan'}"




class MarketplaceConfigurationPayoutAutomationStrategyEnum(models.TextChoices):
    MANUAL = 'MANUAL', 'Completely Manually controlled Payout Status'
    AUTOMATED_BY_FULFILLMENT = 'AUTOMATED_BY_FULFILLMENT', 'Ready for payout when status is paid and fulfilled'


class MarketplaceConfigurationCurrencyEnum(models.TextChoices):
    USD = 'USD', 'US Dollar'
    EUR = 'EUR', 'Euro'
    GBP = 'GBP', 'British Pound'
    


class VariantUniquenessEnum(models.TextChoices):
    UNIQUE = 'UNIQUE', 'Unique'
    NON_UNIQUE = 'NON_UNIQUE', 'Non-Unique'


class RevenueAccrualStrategyEnum(models.TextChoices):
    ON_PAYMENT = 'ON_PAYMENT', 'On Payment'
    ON_FULFILLMENT = 'ON_FULFILLMENT', 'On Fulfillment'


class AvailableShippingStrategyEnum(models.TextChoices):
    MARKETPLACE_ONLY = 'MARKETPLACE_ONLY', 'Marketplace Only'
    SELLER_ONLY = 'SELLER_ONLY', 'Seller Only'
    HYBRID = 'HYBRID', 'Hybrid'


class MarketplaceConfigurationAttributeTemplateStrategy(models.TextChoices):
    GLOBAL = 'GLOBAL', 'Global'
    SELLER = 'SELLER', 'Seller'




class MarketplaceConfiguration(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey('core.Tenant', on_delete=models.CASCADE)
    marketplace_name = models.CharField(max_length=255)
    require_product_approval = models.BooleanField(default=False)
    require_product_types = models.BooleanField(default=False)
    payout_automation_strategy = models.CharField(
        max_length=50,
        choices=MarketplaceConfigurationPayoutAutomationStrategyEnum.choices,
        null=True
    )
    domiciled_currency = models.CharField(
        max_length=3,
        choices=MarketplaceConfigurationCurrencyEnum.choices
    )
    supported_currencies = ArrayField(
        models.CharField(max_length=3),
        default=list
    )
    default_country = models.CharField(max_length=2)
    supported_countries = ArrayField(
        models.CharField(max_length=2),
        default=list
    )
    seller_can_send_quote = models.BooleanField(default=False)
    variant_uniqueness = models.CharField(
        max_length=50,
        choices=VariantUniquenessEnum.choices,
        null=True
    )
    enable_stock_allocation_for_quotes = models.BooleanField(default=False)
    enable_stock_allocation_for_offers = models.BooleanField(null=True)
    enable_stock_allocation_for_drafts = models.BooleanField(default=False)
    validate_stock_on_order_payment_creation = models.BooleanField(default=False)
    timezone = models.CharField(max_length=100)
    enable_backorders = models.BooleanField(default=False)
    revenue_accrual_strategy = models.CharField(
        max_length=50,
        choices=RevenueAccrualStrategyEnum.choices,
        null=True
    )
    available_shipping_strategy = models.CharField(
        max_length=50,
        choices=AvailableShippingStrategyEnum.choices,
        null=True
    )
    attribute_template_strategy = models.CharField(
        max_length=50,
        choices=MarketplaceConfigurationAttributeTemplateStrategy.choices
    )
    fulfillment_model = models.CharField(
        max_length=50,
        choices=FulfillmentModelEnum.choices
    )
    default_weight_unit = models.CharField(
        max_length=50,
        choices=WeightUnitsEnum.choices,
        null=True
    )
    automatic_fulfillment_digital_products = models.BooleanField(default=False)
    default_digital_max_downloads = models.IntegerField(null=True)
    default_digital_url_valid_days = models.IntegerField(null=True)
    track_inventory_by_default = models.BooleanField(default=True)
    description = models.TextField()
    name = models.CharField(max_length=255)
    company_address = models.ForeignKey(
        'core.Address',
        on_delete=models.SET_NULL,
        null=True,
        related_name='marketplace_configurations'
    )
    default_mail_sender_name = models.CharField(max_length=255, null=True)
    default_mail_sender_address = models.EmailField(null=True)
    default_mail_support_address = models.EmailField(null=True)
    customer_set_password_url = models.URLField(null=True)
    include_taxes_in_prices = models.BooleanField(default=True)
    charge_taxes_on_shipping = models.BooleanField(default=True)

    class Meta:
        db_table = 'marketplace_configuration'

    def __str__(self):
        return f"{self.marketplace_name} Configuration"


class FulfillmentModelEnum(models.TextChoices):
    FULFILLED_BY_MARKETPLACE = 'FULFILLED_BY_MARKETPLACE', 'Fulfilled by marketplace'
    FULFILLED_BY_SELLER = 'FULFILLED_BY_SELLER', 'Fulfilled by seller'
    HYBRID = 'HYBRID', 'Hybrid'