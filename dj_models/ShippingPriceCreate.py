class ShippingPriceCreate(models.Model):
    shippingZone = models.ShippingZone()
    shippingErrors = models.ShippingError()
    shippingMethod = models.ShippingMethod()

