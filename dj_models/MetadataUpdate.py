class MetadataUpdate(models.Model):
    metadataErrors = models.MetadataError()
    item = models.ObjectWithMetadata()

