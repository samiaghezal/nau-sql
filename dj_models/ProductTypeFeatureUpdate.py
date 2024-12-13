class ProductTypeFeatureUpdate(models.Model):
    productType = models.ProductType()
    productErrors = models.ProductError()

