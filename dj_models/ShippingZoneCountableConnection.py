class ShippingZoneCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.ShippingZoneCountableEdge()
    totalCount = models.Int()

