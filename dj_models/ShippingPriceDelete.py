class ShippingPriceDelete(models.Model):
    shippingMethod = models.ShippingMethod()
    shippingZone = models.ShippingZone()
    shippingErrors = models.ShippingError()

