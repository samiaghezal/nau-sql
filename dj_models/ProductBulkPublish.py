class ProductBulkPublish(models.Model):
    count = models.Int()
    productErrors = models.ProductError()
