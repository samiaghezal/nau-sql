class DocumentAttach(models.Model):
    document = models.Document()
    instances = models.DocumentTargetInstance()
    documentErrors = models.DocumentError()

