from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import JSONField
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey

from ...core.models import ModelWithMetadata

User = get_user_model()


class Content(ModelWithMetadata):
    publication_date = models.DateField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True)
    is_page = models.BooleanField(default=False)
    locked_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='locked_content'
    )
    lock_expiry = models.DateTimeField(null=True, blank=True)
    data = JSONField(default=dict)
    draft_data = JSONField(default=dict)
    revision = models.IntegerField(default=1)
    has_active_draft = models.BooleanField(null=True)
    
    # Optional one-to-one relationship with ContentPageData
    content_page_data = models.OneToOneField(
        'ContentPageData',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='content'
    )

    class Meta:
        db_table = 'content'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['is_published']),
        ]

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        # Update has_active_draft based on data vs draft_data
        if not self.has_active_draft:
            self.has_active_draft = self.data != self.draft_data
        super().save(*args, **kwargs)

    def publish(self):
        """Publish the content by copying draft data to live data"""
        self.data = self.draft_data
        self.is_published = True
        self.publication_date = timezone.now().date()
        self.has_active_draft = False
        self.save()

    def create_draft(self, data):
        """Create a new draft version"""
        self.draft_data = data
        self.revision += 1
        self.has_active_draft = True
        self.save()

    def discard_draft(self):
        """Discard the draft by copying live data back to draft"""
        self.draft_data = self.data
        self.has_active_draft = False
        self.save()


class Media(ModelWithMetadata):
    tenant = models.ForeignKey(
        'core.Tenant',
        on_delete=models.CASCADE,
        related_name='media'
    )
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    alt = models.CharField(max_length=255)

    class Meta:
        db_table = 'media'
        verbose_name_plural = 'media'

    def __str__(self):
        return self.title


class Menu(ModelWithMetadata):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        db_table = 'menu'

    def __str__(self):
        return self.name


class MenuItem(MPTTModel, ModelWithMetadata):
    menu = models.ForeignKey(
        Menu,
        related_name='items',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        'product.Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    collection = models.ForeignKey(
        'product.Collection',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    page = models.ForeignKey(
        'Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    url = models.URLField(null=True, blank=True)

    class Meta:
        db_table = 'menu_item'

    def __str__(self):
        return self.name


class Page(ModelWithMetadata):
    publication_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    content_html = models.TextField()
    seo_title = models.CharField(max_length=255, null=True, blank=True)
    seo_description = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    is_published = models.BooleanField(default=False)

    class Meta:
        db_table = 'page'
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['is_published']),
        ]

    def __str__(self):
        return self.title


class PageInfo(models.Model):
    has_next_page = models.BooleanField(default=False)
    has_previous_page = models.BooleanField(default=False)
    start_cursor = models.CharField(max_length=255, null=True, blank=True)
    end_cursor = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'page_info'
        managed = False  # This is typically handled by GraphQL pagination
