class ExportError(models.Model):
    field = models.String()
    message = models.String()
    code = models.ExportErrorCode()
