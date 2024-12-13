class PrivateMetadataUpdate(models.Model):
    metadataErrors = models.MetadataError()
    item = models.ObjectWithMetadata()

