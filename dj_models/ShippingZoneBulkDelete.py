class ShippingZoneBulkDelete(models.Model):
    count = models.Int()
    shippingErrors = models.ShippingError()

