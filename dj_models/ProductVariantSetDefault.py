class ProductVariantSetDefault(models.Model):
    product = models.Product()
    productErrors = models.ProductError()

