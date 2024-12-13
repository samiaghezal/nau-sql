class MetadataDelete(models.Model):
    metadataErrors = models.MetadataError()
    item = models.ObjectWithMetadata()

