class ProductStatusLog(models.Model):
    user = models.User()
    subStatus = models.ProductSubStatusEnum()
    subStatusReason = models.String()
    createdAt = models.DateTime()
    id = models.ID()
    privateMetadata = models.MetadataItem()
    metadata = models.MetadataItem()

