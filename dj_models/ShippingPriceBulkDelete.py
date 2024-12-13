class ShippingPriceBulkDelete(models.Model):
    count = models.Int()
    shippingErrors = models.ShippingError()

