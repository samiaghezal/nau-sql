class ProductSetLocationType(models.Model):
    product = models.Product()
    location = models.Location()
    productErrors = models.ProductError()

