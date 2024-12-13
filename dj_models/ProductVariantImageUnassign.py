class ProductVariantImageUnassign(models.Model):
    productVariant = models.ProductVariant()
    image = models.ProductImage()
    productErrors = models.ProductError()

