class ProductTypeReorderAttributes(models.Model):
    productType = models.ProductType()
    productErrors = models.ProductError()

