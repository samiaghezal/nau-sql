class ProductBulkDelete(models.Model):
    count = models.Int()
    productErrors = models.ProductError()

