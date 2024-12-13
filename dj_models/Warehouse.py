class Warehouse(models.Model):
    externalId = models.String()
    externalSource = models.String()
    id = models.ID()
    name = models.String()
    slug = models.String()
    companyName = models.String()
    shippingZones = models.ShippingZoneCountableConnection()
    address = models.Address()
    email = models.String()
    seller = models.Seller()
    privateMetadata = models.MetadataItem()
    metadata = models.MetadataItem()

