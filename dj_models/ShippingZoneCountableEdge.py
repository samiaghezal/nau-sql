class ShippingZoneCountableEdge(models.Model):
    node = models.ShippingZone()
    cursor = models.String()

