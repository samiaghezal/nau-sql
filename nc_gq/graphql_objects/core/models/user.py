from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django_countries.fields import CountryField

from ...core.models import ModelWithMetadata, PermissionEnum


class UserPermission(models.Model):
    code = models.CharField(
        max_length=100,
        choices=PermissionEnum.choices
    )
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        'User',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='permissions'
    )

    class Meta:
        db_table = 'user_permission'

    def __str__(self):
        return f"{self.name} ({self.code})"


class User(AbstractUser, ModelWithMetadata):
    external_id = models.CharField(max_length=255, null=True, blank=True)
    external_source = models.CharField(max_length=255, null=True, blank=True)
    external_payout_account_id = models.CharField(max_length=255, null=True, blank=True)
    external_payout_source = models.CharField(max_length=255, null=True, blank=True)
    external_payout_onboarding_url = models.URLField(null=True, blank=True)
    company_name = models.CharField(max_length=255)
    note = models.TextField(null=True, blank=True)
    last_status_changed_at = models.DateTimeField(null=True, blank=True)
    default_shipping_address = models.ForeignKey(
        'core.Address',
        related_name='users_shipping',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    default_billing_address = models.ForeignKey(
        'core.Address',
        related_name='users_billing',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    personal_phone = models.CharField(max_length=50, null=True, blank=True)
    tax_exempt_code = models.CharField(max_length=255, null=True, blank=True)
    vat_identification_number = models.CharField(max_length=255, null=True, blank=True)
    seller = models.OneToOneField(
        'commerce.Seller',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user'
    )
    is_assignable = models.BooleanField(default=True)
    price_book = models.ForeignKey(
        'commerce.PriceBook',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users'
    )
    dashboard_embedding_token = models.CharField(max_length=255, null=True, blank=True)
    custom_fields = ArrayField(
        models.JSONField(),
        default=list,
        blank=True
    )

    class Meta:
        db_table = 'user'
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['external_id']),
            models.Index(fields=['company_name']),
        ]

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()


class UserType(ModelWithMetadata):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    default_shipping_address = models.ForeignKey(
        'core.Address',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_types'
    )

    class Meta:
        db_table = 'user_type'

    def __str__(self):
        return self.email or f"UserType {self.id}"
