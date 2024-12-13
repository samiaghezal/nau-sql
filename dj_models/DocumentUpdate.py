class DocumentUpdate(models.Model):
    document = models.Document()
    documentErrors = models.DocumentError()

