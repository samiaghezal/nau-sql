class BulkProductError(models.Model):
    field = models.String()
    message = models.String()
    code = models.ProductErrorCode()
    attributes = models.ID()
    index = models.Int()
    warehouses = models.ID()
