class PrivateMetadataDelete(models.Model):
    metadataErrors = models.MetadataError()
    item = models.ObjectWithMetadata()

