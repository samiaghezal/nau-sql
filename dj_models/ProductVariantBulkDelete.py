class ProductVariantBulkDelete(models.Model):
    count = models.Int()
    productErrors = models.ProductError()

