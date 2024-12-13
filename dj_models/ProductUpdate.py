class ProductUpdate(models.Model):
    productErrors = models.ProductError()
    product = models.Product()

