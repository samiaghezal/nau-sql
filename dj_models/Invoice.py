class Invoice(models.Model):
    id = models.ID()
    metadata = models.MetadataItem()
    status = models.JobStatusEnum()
    number = models.String()
    externalUrl = models.String()
    isValid = models.Boolean()
    isEditable = models.Boolean()
    privateMetadata = models.MetadataItem()
    createdAt = models.DateTime()
    updatedAt = models.DateTime()
    message = models.String()
    url = models.String()

