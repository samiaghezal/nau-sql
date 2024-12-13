class DocumentRemove(models.Model):
    instances = models.DocumentTargetInstance()
    documentErrors = models.DocumentError()

