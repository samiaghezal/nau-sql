class ShippingMethod(models.Model):
    id = models.ID()
    privateMetadata = models.MetadataItem()
    metadata = models.MetadataItem()
    name = models.String()
    price = models.Money()
    minimumOrderPrice = models.Money()
    maximumOrderPrice = models.Money()
    minimumOrderWeight = models.Weight()
    maximumOrderWeight = models.Weight()
    type = models.ShippingMethodTypeEnum()
    requiresSecondaryAddress = models.Boolean()

