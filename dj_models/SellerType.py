class SellerType(models.Model):
    id = models.ID()
    privateMetadata = models.MetadataItem()
    metadata = models.MetadataItem()
    pk = models.Int()
    companyName = models.String()
    owner = models.UserType()

