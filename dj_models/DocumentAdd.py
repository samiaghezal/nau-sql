class DocumentAdd(models.Model):
    document = models.Document()
    instances = models.DocumentTargetInstance()
    documentErrors = models.DocumentError()

