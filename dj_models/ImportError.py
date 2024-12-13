class ImportError(models.Model):
    field = models.String()
    message = models.String()
    code = models.ImportErrorCode()

