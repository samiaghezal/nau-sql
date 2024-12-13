class AddressType(models.Model):
    id = models.ID()
    privateMetadata = models.MetadataItem()
    metadata = models.MetadataItem()
    firstName = models.String()
    lastName = models.String()
    streetAddress1 = models.String()
    streetAddress2 = models.String()
    city = models.String()
    postalCode = models.String()
    country = models.String()
    countryArea = models.String()
    phone = models.String()

