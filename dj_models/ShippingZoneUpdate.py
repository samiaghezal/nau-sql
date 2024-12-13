class ShippingZoneUpdate(models.Model):
    shippingErrors = models.ShippingError()
    shippingZone = models.ShippingZone()

