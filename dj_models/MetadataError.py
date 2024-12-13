class MetadataError(models.Model):
    field = models.String()
    message = models.String()
    code = models.MetadataErrorCode()

