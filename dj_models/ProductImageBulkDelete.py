class ProductImageBulkDelete(models.Model):
    count = models.Int()
    productErrors = models.ProductError()

