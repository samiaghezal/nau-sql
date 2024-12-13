class TypeformFormAttachment(models.Model):
    type = models.String()
    href = models.String()
    properties = models.TypeformFormProperties()

