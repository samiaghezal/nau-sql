class ProductTypeFeatureCreate(models.Model):
    productType = models.ProductType()
    productErrors = models.ProductError()

