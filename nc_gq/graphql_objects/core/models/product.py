from django.db import models
from django.contrib.postgres.fields import ArrayField
from django_measurement.models import MeasurementField
from measurement.measures import Weight
from django_prices.models import MoneyField, TaxedMoneyField
from django.utils import timezone
import uuid

from ...core.models import ModelWithMetadata


class ProductStatus(models.TextChoices):
    DRAFT = 'DRAFT', 'Draft'
    ACTIVE = 'ACTIVE', 'Active'
    INACTIVE = 'INACTIVE', 'Inactive'


class ProductSubStatus(models.TextChoices):
    PENDING_APPROVAL = 'PENDING_APPROVAL', 'Pending Approval'
    APPROVED = 'APPROVED', 'Approved'
    REJECTED = 'REJECTED', 'Rejected'
    # Add other sub-statuses as needed


class Product(ModelWithMetadata):
    publication_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    description_html = models.TextField()
    external_id = models.CharField(max_length=255, null=True, blank=True)
    external_source = models.CharField(max_length=255, null=True, blank=True)
    seller = models.ForeignKey(
        'commerce.Seller',
        on_delete=models.SET_NULL,
        null=True,
        related_name='products'
    )
    mpn = models.CharField(max_length=255, null=True, blank=True)
    brand = models.CharField(max_length=255, null=True, blank=True)
    manufacturer = models.CharField(max_length=255, null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    seo_title = models.CharField(max_length=255, null=True, blank=True)
    seo_description = models.TextField(null=True, blank=True)
    product_type = models.ForeignKey(
        'ProductType',
        on_delete=models.CASCADE,
        related_name='products'
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        related_name='products'
    )
    currency = models.CharField(max_length=3)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    charge_taxes = models.BooleanField(default=True)
    weight = MeasurementField(measurement=Weight, null=True, blank=True)
    available_for_purchase = models.DateField(null=True, blank=True)
    visible_in_listings = models.BooleanField(default=True)
    default_variant = models.OneToOneField(
        'ProductVariant',
        related_name='default_for_product',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    override_price = models.BooleanField(default=False)
    override_currency = models.BooleanField(default=False)
    status = models.CharField(
        max_length=50,
        choices=ProductStatus.choices,
        default=ProductStatus.DRAFT
    )
    sub_status = models.CharField(
        max_length=50,
        choices=ProductSubStatus.choices,
        default=ProductSubStatus.PENDING_APPROVAL
    )
    is_price_override_allowed = models.BooleanField(default=False)
    is_shipping_required = models.BooleanField(default=True)
    is_digital = models.BooleanField(default=False)
    tax_type = models.ForeignKey(
        'core.TaxType',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    custom_fields = ArrayField(
        models.JSONField(),
        default=list,
        blank=True
    )
    sort_order = models.IntegerField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    origin_location = models.ForeignKey(
        'warehouse.Location',
        on_delete=models.SET_NULL,
        null=True,
        related_name='products_as_origin'
    )
    destination_location = models.ForeignKey(
        'warehouse.Location',
        on_delete=models.SET_NULL,
        null=True,
        related_name='products_as_destination'
    )
    primary_location = models.ForeignKey(
        'warehouse.Location',
        on_delete=models.SET_NULL,
        null=True,
        related_name='primary_products'
    )
    sort_priority_weight = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'product'
        ordering = ['name']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['name']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return self.name

    @property
    def is_available(self):
        return (
            self.status == ProductStatus.ACTIVE and
            self.sub_status == ProductSubStatus.APPROVED and
            (not self.available_for_purchase or 
             self.available_for_purchase <= timezone.now().date())
        )


class ProductCategoryReport(models.Model):
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='reports'
    )
    totals = models.IntegerField()
    gross_revenue = models.FloatField()
    quantity_ordered = models.IntegerField()
    avg_price_gross_amount = models.FloatField()
    max_price_gross_amount = models.FloatField()
    min_price_gross_amount = models.FloatField()
    revenue = models.FloatField()
    avg_price = models.FloatField()
    max_price = models.FloatField()
    min_price = models.FloatField()
    product_category_id = models.IntegerField()

    class Meta:
        db_table = 'product_category_report'
        managed = False  # This is typically handled by reporting system

    def __str__(self):
        return f"Report for {self.category.name}"


class FeatureTypeEnum(models.TextChoices):
    TEXT = 'TEXT', 'Text'
    SELECT = 'SELECT', 'Select'
    MULTISELECT = 'MULTISELECT', 'Multi Select'
    # Add other feature types as needed


class ProductVariantStatus(models.TextChoices):
    DRAFT = 'DRAFT', 'Draft'
    ACTIVE = 'ACTIVE', 'Active'
    INACTIVE = 'INACTIVE', 'Inactive'


class ProductVariantSubStatus(models.TextChoices):
    PENDING_APPROVAL = 'PENDING_APPROVAL', 'Pending Approval'
    APPROVED = 'APPROVED', 'Approved'
    REJECTED = 'REJECTED', 'Rejected'


class ProductFeature(ModelWithMetadata):
    sort_order = models.IntegerField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by_user = models.ForeignKey(
        'core.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='deleted_features'
    )
    deleted_by_app = models.ForeignKey(
        'app.App',
        on_delete=models.SET_NULL,
        null=True,
        related_name='deleted_features'
    )
    deletion_batch_uuid = models.UUIDField(null=True, blank=True)
    tenant = models.ForeignKey('core.Tenant', on_delete=models.CASCADE)
    feature_type = models.CharField(
        max_length=50,
        choices=FeatureTypeEnum.choices
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    options = ArrayField(
        models.CharField(max_length=255),
        null=True,
        blank=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='features'
    )
    product_type_feature = models.ForeignKey(
        'ProductTypeProductFeature',
        on_delete=models.SET_NULL,
        null=True,
        related_name='product_features'
    )

    class Meta:
        db_table = 'product_feature'
        ordering = ['sort_order', 'name']


class ProductImage(ModelWithMetadata):
    sort_order = models.IntegerField(null=True, blank=True)
    external_id = models.CharField(max_length=255, null=True, blank=True)
    external_source = models.CharField(max_length=255, null=True, blank=True)
    alt = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey(
        Product,
        related_name='images',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'product_image'
        ordering = ['sort_order']


class ProductStatusLog(ModelWithMetadata):
    user = models.ForeignKey(
        'core.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='product_status_logs'
    )
    sub_status = models.CharField(
        max_length=50,
        choices=ProductSubStatus.choices,
        null=True
    )
    sub_status_reason = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='status_logs'
    )

    class Meta:
        db_table = 'product_status_log'
        ordering = ['-created_at']


class ProductType(ModelWithMetadata):
    external_id = models.CharField(max_length=255, null=True, blank=True)
    external_source = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    is_shipping_required = models.BooleanField(default=True)
    is_digital = models.BooleanField(default=False)
    weight = MeasurementField(measurement=Weight, null=True, blank=True)
    is_price_override_allowed = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        'commerce.Seller',
        on_delete=models.SET_NULL,
        null=True,
        related_name='product_types'
    )
    tax_type = models.ForeignKey(
        'core.TaxType',
        on_delete=models.SET_NULL,
        null=True
    )
    has_variants = models.BooleanField(default=True)
    model = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'product_type'
        ordering = ['name']

    def __str__(self):
        return self.name


class ProductVariant(ModelWithMetadata):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
    description_html = models.TextField()
    external_id = models.CharField(max_length=255, null=True, blank=True)
    external_source = models.CharField(max_length=255, null=True, blank=True)
    seo_title = models.CharField(max_length=255, null=True, blank=True)
    seo_description = models.TextField(null=True, blank=True)
    sku = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    nautical_stock_number = models.CharField(max_length=255)
    status = models.CharField(
        max_length=50,
        choices=ProductVariantStatus.choices,
        default=ProductVariantStatus.DRAFT
    )
    sub_status = models.CharField(
        max_length=50,
        choices=ProductVariantSubStatus.choices,
        default=ProductVariantSubStatus.PENDING_APPROVAL
    )
    currency = models.CharField(max_length=3, null=True, blank=True)
    product = models.ForeignKey(
        Product,
        related_name='variants',
        on_delete=models.CASCADE
    )
    track_inventory = models.BooleanField(default=True)
    weight = MeasurementField(measurement=Weight, null=True, blank=True)
    seller = models.ForeignKey(
        'commerce.Seller',
        on_delete=models.SET_NULL,
        null=True,
        related_name='variants'
    )
    published_at = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    override_currency = models.BooleanField(default=False)
    requires_quote = models.BooleanField(default=False)
    allow_backorders = models.BooleanField(null=True)
    is_price_override_allowed = models.BooleanField(default=False)
    is_shipping_required = models.BooleanField(default=True)
    is_digital = models.BooleanField(default=False)
    price = MoneyField(max_digits=10, decimal_places=2, currency_field='currency', null=True)
    cost_price = MoneyField(max_digits=10, decimal_places=2, currency_field='currency', null=True)
    margin = models.IntegerField(null=True, blank=True)
    quantity_ordered = models.IntegerField(default=0)
    country_code = models.CharField(max_length=2, null=True, blank=True)
    net_revenue = models.FloatField(null=True, blank=True)
    gross_revenue = models.FloatField(null=True, blank=True)
    sort_order_in_collection = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'product_variant'
        ordering = ['name']
        indexes = [
            models.Index(fields=['sku']),
            models.Index(fields=['nautical_stock_number']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return f"{self.product.name} - {self.name}"

    @property
    def is_visible(self):
        return (
            self.is_published and
            self.published_at and
            self.published_at <= timezone.now()
        )
