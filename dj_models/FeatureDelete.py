class FeatureDelete(models.Model):
    product = models.Product()
    variant = models.ProductVariant()
    productErrors = models.ProductError()

