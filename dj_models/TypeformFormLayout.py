class TypeformFormLayout(models.Model):
    type = models.String()
    placement = models.String()
    attachment = models.TypeformFormAttachment()

