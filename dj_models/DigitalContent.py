class DigitalContent(models.Model):
    useDefaultSettings = models.Boolean()
    automaticFulfillment = models.Boolean()
    productVariant = models.ProductVariant()
    contentFile = models.String()
    maxDownloads = models.Int()
    urlValidDays = models.Int()
    urls = models.DigitalContentUrl()
    id = models.ID()
    privateMetadata = models.MetadataItem()
    metadata = models.MetadataItem()

