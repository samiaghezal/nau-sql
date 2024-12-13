class UserType(models.Model):
    id = models.ID()
    privateMetadata = models.MetadataItem()
    metadata = models.MetadataItem()
    firstName = models.String()
    lastName = models.String()
    email = models.String()
    defaultShippingAddress = models.AddressType()

